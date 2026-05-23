"""Project pipeline registry."""

from kedro.pipeline import Pipeline

from si_image_processing.pipelines.image_processing import create_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines."""
    image_processing_pipeline = create_pipeline()
    return {
        "__default__": image_processing_pipeline,
        "image_processing": image_processing_pipeline,
    }
