from pathlib import Path
from PIL import Image


def load_image(path: str) -> Image.Image:
    """
    Lädt ein Bild von der Festplatte.

    - path: Dateiname oder Pfad zum Bild (z.B. 'test.jpg')
    - Rückgabe: PIL.Image-Objekt
    """
    img_path = Path(path)       # String path zu Path-Objekt
    if not img_path.exists():
        raise FileNotFoundError(f"File {img_path} does not exist")
    return Image.open(img_path)

