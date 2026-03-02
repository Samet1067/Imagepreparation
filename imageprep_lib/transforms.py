from PIL import Image
import numpy as np
from PIL import ImageEnhance


def to_grayscale(img: Image.Image) -> Image.Image:
    """
        Wandelt ein Farb-Bild (RGB) in ein Graustufen-Bild um.

        - Input:  PIL.Image mit Modus z.B. "RGB"
        - Output: PIL.Image mit Modus "L" (Luminanz = Helligkeit)
    """
    gray = img.convert("L")
    return gray

def resize_image(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    """
        Skaliert ein Bild auf eine neue Größe.

        - size: (Breite, Höhe), z.B. (256, 256)
    """
    resized = img.resize(size)
    return resized

def normalize_to_float(img: Image.Image) -> np.ndarray:
    """
        Wandelt ein Bild in ein NumPy-Array um und skaliert die Pixelwerte in [0.0, 1.0].

        Rückgabe:
        - NumPy-Array (z.B. Form (H, W) oder (H, W, C)) mit dtype float32
    """
    arr = np.asarray(img).astype("float32") # erst zu float
    arr /= 255.0                            # dann normalisieren
    return arr

def change_brightness(img: Image.Image, factor: float) -> Image.Image:
    """
        Passt die Helligkeit des Bildes an.

        - factor < 1.0  -> dunkler
        - factor = 1.0  -> unverändert
        - factor > 1.0  -> heller
    """
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)

def change_contrast(img: Image.Image, factor: float) -> Image.Image:
    """
    Passt den Kontrast des Bildes an.

    - factor < 1.0  -> weniger Kontrast (flacher)
    - factor = 1.0  -> unverändert
    - factor > 1.0  -> mehr Kontrast (knackiger)
    """
    enhancer = ImageEnhance.Contrast(img)
    return enhancer.enhance(factor)

def flip_horizontal(img: Image.Image) -> Image.Image:
    """
    Spiegelt das Bild horizontal (links/rechts).
    """
    return img.transpose(Image.FLIP_LEFT_RIGHT)