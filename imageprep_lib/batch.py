from pathlib import Path
from typing import Callable

from .io import load_image
from .transforms import to_grayscale, resize_image, change_brightness, change_contrast



def process_folder(
    input_dir: str,
    output_dir: str,
    size: tuple[int, int] = (256, 256),
    brightness: float = 1.0,
    contrast: float = 1.0,
) -> None:
    """
    Verarbeitet alle Bilder in einem Eingabe-Ordner und speichert
    die bearbeiteten Versionen im Ausgabe-Ordner.

    Schritte:
    - Bild laden
    - Graustufen
    - Resize
    - Helligkeit & Kontrast anpassen
    - Speichern
    """
    in_path = Path(input_dir)
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # Alle Dateien im input_dir durchgehen
    for img_path in in_path.iterdir():
        if img_path.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            continue  # andere Dateien ignorieren

        img = load_image(str(img_path))

        # Pipeline-Schritte
        img_proc = to_grayscale(img)
        img_proc = resize_image(img_proc, size)
        img_proc = change_brightness(img_proc, brightness)
        img_proc = change_contrast(img_proc, contrast)

        # Ziel-Dateinamen bauen
        out_file = out_path / img_path.name

        # Speichern
        img_proc.save(out_file)
        print(f"Gespeichert: {out_file}")