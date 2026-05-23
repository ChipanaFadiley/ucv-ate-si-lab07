"""Pipeline definition for image processing."""

from kedro.pipeline import Pipeline, node

from .nodes import process_image


def create_pipeline(**kwargs) -> Pipeline:
    """Create the image processing pipeline."""
    return Pipeline(
        [
            node(
                func=process_image,
                inputs=[
                    "params:input_path",
                    "params:output_path",
                    "params:rotation_angle",
                    "params:filter_name",
                    "params:watermark_text",
                    "params:watermark_font_size",
                ],
                outputs="processed_image",
                name="process_image_node",
            )
        ]
    )
