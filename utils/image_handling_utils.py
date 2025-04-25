from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageOps
from pyvips import Image as VipsImage


def get_histogram(
    img: Path,
    v_line: int | None = None,
):
    """
    Generates a simple color distribution histogram for a grayscale image and plots it.
    """
    img = Image.open(img)
    
    gray = ImageOps.grayscale(img)
    gray_np = np.array(gray)

    # Generate histogram
    hist, _ = np.histogram(gray_np.flatten(), bins=256, range=(0, 256))

    plt.plot(hist, color='black')
    plt.xlim([0, 255])
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.title('Histogram of Grayscale Image')
    if v_line is not None:
        plt.axvline(x=v_line, color='red', linestyle='--', label=f'Threshold: {v_line}')
        plt.legend()
    plt.show()


def save_wsi(
    img_array: np.ndarray,
    img_path: Path,
):
    """
    Saves a numpy array of a WSI as a pyramidal TIFF using pyvips.
    """
    vips_img = VipsImage.new_from_memory(img_array.data, img_array.shape[1], img_array.shape[0], 1, "uchar")
    vips_img.tiffsave(
        img_path.parent / Path(img_path.stem + '_mask.tiff'),
        tile=True,
        compression="jpeg",
        bigtiff=True,
        pyramid=True,
        tile_width=512,
        tile_height=512,
        Q=90,
        predictor="horizontal",
        strip=True,
    )


def save_img(
    img_array: np.ndarray,
    img_path: Path,
):
    """
    Saves a numpy array as a PNG image.
    """
    img = Image.fromarray(img_array)
    img.save(img_path.parent / Path(img_path.stem + '_mask.png'), format='PNG')
