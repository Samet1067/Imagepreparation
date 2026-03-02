# Image Preparation Pipeline for Vehicle Images

## Overview

This project implements a modular image preprocessing pipeline in Python.
It is designed to simulate automated photo workflows for vehicle images,
as commonly used in automotive retail and AI-based image processing systems.

The pipeline supports:

- Loading vehicle images
- Converting to grayscale
- Resizing to fixed dimensions
- Adjusting brightness and contrast
- Horizontal flipping (data augmentation)
- Normalizing pixel values for machine learning
- Batch-processing entire folders of images

The goal of this project is to demonstrate structured software design
and basic computer vision preprocessing techniques for AI workflows.

---

## Project Structure
imageprep
├── imageprep_lib
│   ├── io.py
│   ├── transforms.py
│   ├── visualize.py
│   └── batch.py
├── main.py
├── cars_input/
├── cars_output/
└── README.md

### Modules

- **io.py**  
  Handles image loading from disk.

- **transforms.py**  
  Contains image preprocessing functions:
  - Grayscale conversion
  - Resize
  - Brightness adjustment
  - Contrast adjustment
  - Normalization

- **visualize.py**  
  Functions for displaying images.

- **batch.py**  
  Automates processing of entire image folders.

- **main.py**  
  Entry point for running single-image or batch demos.

---

## Example: Single Image Processing

The pipeline performs the following steps:

1. Load image
2. Convert to grayscale
3. Resize to 256x256
4. Adjust brightness and contrast
5. Normalize pixel values to [0,1]

This simulates preparation of vehicle images for AI-based systems.

---

## Example: Batch Processing

To process all images in a folder:

1. Place vehicle images inside `cars_input/`
2. Run `run_batch_demo()` in `main.py`
3. Processed images will be saved in `cars_output/`

This simulates automated photo workflows in automotive environments.

---

## Technologies Used

- Python 3
- Pillow (PIL)
- NumPy
- Matplotlib
- Git / GitHub

---

