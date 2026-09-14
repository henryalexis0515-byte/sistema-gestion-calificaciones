# Sistema de Gestión de Calificaciones

Proyecto desarrollado como parte de la actividad ACA de la asignatura Calidad de Software.

## Descripción

El sistema fue desarrollado en Python y permite realizar operaciones básicas relacionadas con la gestión de calificaciones académicas, incluyendo el cálculo del promedio, la determinación del estado académico y la validación del rango permitido para las notas.

## Pruebas unitarias

Para validar el funcionamiento del sistema se implementaron tres casos de prueba utilizando el módulo `unittest` de Python:

- CP-01: Cálculo correcto del promedio.
- CP-02: Determinación del estado académico.
- CP-03: Validación de una calificación fuera del rango permitido.

## Estructura del proyecto

- `calificaciones.py`: contiene las funciones principales del sistema.
- `test_calificaciones.py`: contiene los casos de prueba unitarios.

## Ejecución de las pruebas

Las pruebas pueden ejecutarse desde la terminal utilizando:

python -m unittest test_calificaciones.py -v

## Tecnologías utilizadas

- Python
- unittest
