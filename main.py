"""
main.py

Einstiegspunkt für die Bildaufbereitungs-Pipeline.
Demonstriert:

1. Verarbeitung eines einzelnen Fahrzeugbildes
2. Automatische Batch-Verarbeitung eines Ordners
"""

from imageprep_lib.io import load_image
from imageprep_lib.visualize import show_image
from imageprep_lib.transforms import (
    to_grayscale,
    resize_image,
    normalize_to_float,
    change_brightness,
    change_contrast,
    flip_horizontal,
)
from imageprep_lib.batch import process_folder



# Einzelbild-Demo
def run_single_image_demo():
    """
    Demonstriert die Verarbeitung eines einzelnen Bildes.
    """

    # 1. Bild laden
    img = load_image("cars_input/autohaus.jpg")

    # 2. Vorverarbeitungsschritte
    gray = to_grayscale(img)
    resized = resize_image(gray, (256, 256))
    brighter = change_brightness(resized, 1.1)
    high_contrast = change_contrast(brighter, 1.2)
    flipped = flip_horizontal(high_contrast)

    # 3. Normalisierung für ML
    arr = normalize_to_float(high_contrast)

    print("=== Einzelbild-Demo ===")
    print("Array-Shape:", arr.shape)
    print("Datentyp:", arr.dtype)
    print("Min:", arr.min(), "Max:", arr.max())
    print()

    # 4. Visualisierung
    show_image(img, title="Original")
    show_image(high_contrast, title="Helligkeit + Kontrast angepasst")
    show_image(resized, title="Graustufen 256x256")
    show_image(flipped, title="Gespiegelt")



# Batch-Demo (Ordnerverarbeitung)
def run_batch_demo():
    """
    Verarbeitet automatisch alle Bilder in einem Eingabeordner
    und speichert die bearbeiteten Versionen im Ausgabeordner.
    """

    print("=== Batch-Demo ===")

    process_folder(
        input_dir="cars_input",
        output_dir="cars_output",
        size=(256, 256),
        brightness=1.1,
        contrast=1.2,
    )

    print("Batch-Verarbeitung abgeschlossen.\n")



# Programmstart
if __name__ == "__main__":

    # Wähle hier, was ausgeführt werden soll:

    # run_single_image_demo()
    run_batch_demo()