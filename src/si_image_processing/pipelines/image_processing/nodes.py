"""Nodes for the image processing pipeline."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

SUPPORTED_FILTERS = {
    "BLUR": ImageFilter.BLUR,
    "CONTOUR": ImageFilter.CONTOUR,
    "DETAIL": ImageFilter.DETAIL,
    "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
    "EMBOSS": ImageFilter.EMBOSS,
    "FIND_EDGES": ImageFilter.FIND_EDGES,
    "SHARPEN": ImageFilter.SHARPEN,
    "SMOOTH": ImageFilter.SMOOTH,
}


def _get_filter(filter_name: str) -> ImageFilter.Filter:
    normalized_name = filter_name.upper()
    if normalized_name not in SUPPORTED_FILTERS:
        supported = ", ".join(sorted(SUPPORTED_FILTERS))
        raise ValueError(f"Unsupported filter '{filter_name}'. Supported filters: {supported}")
    return SUPPORTED_FILTERS[normalized_name]


def _load_font(font_size: int) -> ImageFont.ImageFont:
    try:
        return ImageFont.truetype("arial.ttf", size=font_size)
    except OSError:
        return ImageFont.load_default(size=font_size)


def process_image(
    input_path: str,
    output_path: str,
    rotation_angle: float = 45,
    filter_name: str = "EMBOSS",
    watermark_text: str = "UCV - Sistemas Inteligentes",
    watermark_font_size: int = 28,
) -> str:
    """Rotate, filter, watermark, and save an image."""
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)

    with Image.open(input_path) as image:
        rotated = image.convert("RGB").rotate(rotation_angle, expand=True)
        filtered = rotated.filter(_get_filter(filter_name))
        draw = ImageDraw.Draw(filtered)

        if watermark_text:
            draw.text((20, 20), watermark_text, fill="white", font=_load_font(watermark_font_size))

        filtered.save(destination)

    return destination.as_posix()
