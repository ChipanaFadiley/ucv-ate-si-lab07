from kedro.pipeline import Pipeline

from si_image_processing import settings
from si_image_processing.pipeline_registry import register_pipelines
from si_image_processing.pipelines.image_processing import create_pipeline


def test_create_pipeline_registers_process_image_node() -> None:
    pipeline = create_pipeline()

    assert isinstance(pipeline, Pipeline)
    assert [node.name for node in pipeline.nodes] == ["process_image_node"]


def test_register_pipelines_exposes_default_and_named_pipeline() -> None:
    pipelines = register_pipelines()

    assert set(pipelines) == {"__default__", "image_processing"}
    assert pipelines["__default__"] is pipelines["image_processing"]


def test_kedro_settings_point_to_conf_directory() -> None:
    assert settings.CONF_SOURCE == "conf"
    assert settings.CONFIG_LOADER_CLASS.__name__ == "OmegaConfigLoader"
