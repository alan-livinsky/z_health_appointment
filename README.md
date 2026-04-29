# z_health_appointment_custom

## Descripción General

Módulo de **solo vista** para GNU Health. Reordena y reorganiza la vista de árbol (lista) de citas del módulo `health_calendar` sin modificar su código. Aplica sus cambios encima de las extensiones de `health_appointment_fiuner` y `health_appointment_screen_fiuner`, siguiendo el orden de dependencias de Tryton.

No define modelos Python propios — es pura personalización de vista mediante XPath.

## Dependencias

| Módulo | Rol |
|--------|-----|
| `health_calendar` | Vista base de citas |
| `health_appointment_fiuner` | Agrega phone, dni, age, gender, hc, chronic, current_insurance |
| `health_appointment_screen_fiuner` | Agrega botones de pantalla (checked_in, call, in_atention, no_show) |

## Columnas y botones en la vista de árbol

El módulo elimina todos los campos y botones de sus posiciones originales y los reinserta **antes del campo `state`**, en este orden:

| # | Elemento | Tipo | Detalle |
|---|----------|------|---------|
| 1 | **Profesional de Salud** (`healthprof`) | Campo | Ancho 220, expansible |
| 2 | **Especialidad** (`speciality`) | Campo | |
| 3 | **Paciente** (`patient`) | Campo | Ancho 220, expansible |
| 4 | **Fecha** (`appointment_date`) | Campo | Widget `date` |
| 5 | **Hora** (`appointment_date`) | Campo | Widget `time` |
| 6 | **Checked in** | Botón | Paciente llegó y espera |
| 7 | **Llamar** | Botón | Llamar al paciente |
| 8 | **En atención** | Botón | Paciente en consulta |
| 9 | **No show** | Botón | Paciente no se presentó |
| 10 | **Teléfono** (`phone`) | Campo | |
| 11 | **DNI** (`dni`) | Campo | Expansible |
| 12 | **Edad** (`age`) | Campo | Expansible |
| 13 | **Género** (`gender`) | Campo | Expansible |
| 14 | **HC** (`hc`) | Campo | Expansible |
| 15 | **Crónico** (`chronic`) | Campo | Expansible |
| 16 | **Seguro actual** (`current_insurance`) | Campo | Expansible |
| 17 | **Estado** (`state`) | Campo | Al final, posición original |

## Cómo funciona (XPath)

Tryton aplica los XPath en orden de dependencia:

1. `health_appointment_fiuner` corre primero — agrega phone, dni, age, etc.
2. `health_appointment_screen_fiuner` corre segundo — agrega botones de pantalla.
3. **Este módulo corre último** — elimina todos esos elementos de sus posiciones y los reinserta en el orden definido arriba, justo antes del campo `state`.

## Instalación

Requisitos:
- **GNU Health** 4.2.0
- **Tryton** 6.0
- **Python** 3.10.x

Instalar desde el directorio del módulo:

```console
pip install .
```

Modo editable (desarrollo):

```console
pip install -e .
```

## Uso

1. Instalar el módulo con el comando anterior.
2. Ingresar a Tryton como administrador.
3. Ir a **Módulos** y buscar `z_health_appointment`.
4. Activar/actualizar como módulo estándar de Tryton.
5. El orden de columnas se aplica automáticamente en la vista de lista de citas.

## Licencia

**GPL-3.0-or-later** — Software libre bajo la Licencia Pública General de GNU versión 3 o posterior.
