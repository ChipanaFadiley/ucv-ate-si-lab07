# ucv-ate-si-lab07

Pipeline profesional de procesamiento de imagenes desarrollado con Kedro, Poetry, Pillow, GitHub Actions y SonarQube Cloud.

## Descripcion

Este proyecto implementa un flujo reproducible para procesar imagenes mediante un pipeline de Kedro. El proceso toma una imagen de entrada, aplica rotacion, ejecuta un filtro de procesamiento, agrega una marca de agua textual y guarda la imagen resultante.

## Funcionalidades

- Procesamiento de imagenes con Pillow.
- Pipeline reproducible con Kedro.
- Filtro configurable, incluyendo `FIND_EDGES`.
- Angulo de rotacion configurable.
- Marca de agua textual configurable.
- Pruebas unitarias con Pytest.
- Reporte de cobertura con `pytest-cov`.
- Analisis de calidad con Ruff y SonarQube Cloud.
- Automatizacion con GitHub Actions.

## Ejecucion local

Instalar dependencias:

```powershell
poetry install
```

Ejecutar validaciones:

```powershell
poetry run ruff check .
poetry run pytest
```

Ejecutar el pipeline:

```powershell
poetry run kedro run
```

La imagen procesada se genera en `data/03_primary/`.

## Flujo Git recomendado

```text
main
 ↑
Pull Request
 ↑
develop
 ↑
feature/image-processing
```
