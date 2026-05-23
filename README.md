# ucv-ate-si-lab07

Pipeline profesional de procesamiento de imagenes con Kedro, Poetry, GitHub Actions y SonarQube.

## Reto implementado

- Filtro `FIND_EDGES` disponible desde `conf/base/parameters.yml`.
- Angulo de rotacion dinamico mediante `rotation_angle`.
- Marca de agua personalizada mediante `watermark_text`.
- Pruebas unitarias ampliadas con cobertura local del 100%.
- GitHub Actions configurado para ejecutar Ruff, pytest con cobertura XML y analisis de SonarQube Cloud.

## Ejecucion local

```powershell
poetry install
poetry run ruff check .
poetry run pytest
poetry run kedro run
```

La imagen original esta en `data/01_raw/marte.jpg`.
La imagen procesada se genera en `data/03_primary/marte_processed.jpg`.
Kedro tambien guarda la evidencia textual en `data/03_primary/processed_image_path.txt`.

## SonarQube Cloud

El workflow `.github/workflows/build.yml` usa el secreto `SONAR_TOKEN` y ejecuta las pruebas antes del escaneo. La cobertura se publica con:

```properties
sonar.python.coverage.reportPaths=coverage.xml
```

Eso permite que SonarQube Cloud muestre cobertura calculada, no solo el estado del analisis.

## Proteccion de rama main

La proteccion de `main` se configura en GitHub:

1. Ir a `Settings > Branches`.
2. Crear una regla para `main`.
3. Activar pull request obligatorio antes de merge.
4. Activar checks requeridos y seleccionar el workflow `SonarQube`.
5. Guardar la regla.
