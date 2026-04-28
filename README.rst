z_health_appointment
====================

Overview
--------

This module extends GNU Health appointment views with local customizations
without modifying the upstream ``health_calendar`` module.

Features
--------

The custom appointment tree view shows the main columns in this order:

1. Health Professional
2. Patient
3. Date
4. Time
5. Specialty
6. Institution
7. State

Installation
------------

For GNU Health 4.2.0 on Tryton 6.0 with Python 3.10, install the module from
this directory:

.. code-block:: console

   pip install .

Or in editable mode during development:

.. code-block:: console

   pip install -e .

Usage
-----

Once installed, activate ``z_health_appointment`` in Tryton as a normal module
update. The custom column order is then applied to the appointment tree view.

License
-------

SPDX-License-Identifier: GPL-3.0-or-later
