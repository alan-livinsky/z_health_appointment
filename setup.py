#!/usr/bin/env python

from setuptools import setup
import os
import re
import configparser


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8") as f:
        return f.read()


config = configparser.ConfigParser()
with open(os.path.join(os.path.dirname(__file__), 'tryton.cfg'), encoding="utf-8") as cfg:
    config.read_file(cfg)
info = dict(config.items('tryton'))

for key in ('depends', 'extras_depend', 'xml'):
    if key in info:
        info[key] = info[key].strip().splitlines()

major_version, minor_version = 6, 0

requires = []
fiuner_modules = [
    'health_appointment_fiuner',
    'health_appointment_screen_fiuner',
]

for dep in info.get('depends', []):
    if dep == 'health':
        requires.append('gnuhealth == %s' % info.get('version'))
    elif dep in fiuner_modules:
        requires.append('%s == %s' % (dep, info.get('version')))
    elif dep.startswith('health_'):
        health_package = dep.split('_', 1)[1]
        requires.append('gnuhealth_%s == %s' % (health_package, info.get('version')))
    elif not re.match(r'(ir|res|webdav)(\W|$)', dep):
        requires.append(
            'trytond_%s >= %s.%s, < %s.%s'
            % (dep, major_version, minor_version, major_version, minor_version + 1)
        )

requires.append(
    'trytond >= %s.%s, < %s.%s'
    % (major_version, minor_version, major_version, minor_version + 1)
)

setup(
    name='z_health_appointment',
    version=info.get('version', '0.0.1'),
    description='Custom GNU Health appointment view overrides',
    long_description=read('README.rst'),
    author='',
    author_email='',
    url='',
    download_url='',
    package_dir={'trytond.modules.z_health_appointment': '.'},
    packages=[
        'trytond.modules.z_health_appointment',
    ],
    package_data={
        'trytond.modules.z_health_appointment': info.get('xml', [])
        + info.get('translation', [])
        + ['tryton.cfg', 'view/*.xml', 'doc/*.rst', 'locale/*.po', 'icons/*.svg'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
    license='GPL-3',
    install_requires=requires,
    extras_require={},
    python_requires='>=3.10, <3.11',
    zip_safe=False,
    entry_points="""
    [trytond.modules]
    z_health_appointment = trytond.modules.z_health_appointment
    """,
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
)
