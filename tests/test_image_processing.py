from pathlib import Path

import pytest
from PIL import Image

from si_image_processing.pipelines.image_processing import nodes
from si_image_processing.pipelines.image_processing.nodes import _get_filter, process_image


@pytest.fixture
def sample_image(tmp_path: Path) -> Path:
    image_path = tmp_path / "input.jpg"
    image = Image.new("RGB", (80, 40), color="navy")
    image.save(image_path)
    return image_path


def test_process_image_creates_output_with_dynamic_rotation_and_find_edges(
    sample_image: Path, tmp_path: Path
) -> None:
    output_path = tmp_path / "processed.jpg"

    result = process_image(
        str(sample_image),
        str(output_path),
        rotation_angle=90,
        filter_name="FIND_EDGES",
        watermark_text="Marca personalizada",
        watermark_font_size=30,
    )

    assert result == output_path.as_posix()
    assert output_path.exists()

    with Image.open(output_path) as processed:
        assert processed.size == (40, 80)


def test_process_image_accepts_empty_watermark(sample_image: Path, tmp_path: Path) -> None:
    output_path = tmp_path / "processed_without_watermark.jpg"

    result = process_image(
        str(sample_image),
        str(output_path),
        rotation_angle=0,
        filter_name="emboss",
        watermark_text="",
        watermark_font_size=20,
    )

    assert result == output_path.as_posix()
    assert output_path.exists()


def test_get_filter_rejects_unsupported_filter() -> None:
    with pytest.raises(ValueError, match="Unsupported filter"):
        _get_filter("UNKNOWN")


def test_load_font_uses_default_font_when_truetype_is_unavailable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    fallback_font = object()

    def raise_os_error(*args: object, **kwargs: object) -> None:
        raise OSError

    monkeypatch.setattr(nodes.ImageFont, "truetype", raise_os_error)
    monkeypatch.setattr(nodes.ImageFont, "load_default", lambda: fallback_font)

    assert nodes._load_font(28) is fallback_font
