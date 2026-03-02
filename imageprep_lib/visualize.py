import matplotlib.pyplot as plt
from PIL import Image


def show_image(img: Image.Image, title: str = "Bild") -> None:
    """
    Zeigt ein einzelnes Bild mit einem Titel an.
    """
    plt.imshow(img)
    plt.title(title)
    plt.axis("off")
    plt.show()