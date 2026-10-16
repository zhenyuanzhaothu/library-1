# Diffusion Microscopy Video Simulation

This repository contains Python code for generating simulated microscopy images of diffusing particles. The script produces grayscale TIFF image sequences that can be used to construct Videos 2–4 described in the manuscript.

## 1. System Requirements

### Software dependencies

- Python 3.10 or later
- NumPy
- Matplotlib
- Pillow

### Tested operating system

- Windows 11

No non-standard hardware or GPU is required.

## 2. Installation Guide

Clone this repository:

```bash
git clone https://github.com/zhenyuanzhaothu/library-1.git
cd library-1
```

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the required Python packages:

```bash
pip install numpy matplotlib pillow
```

The typical installation time is less than 5 minutes on a standard desktop computer with an existing Python installation and a stable internet connection.

## 3. Demo

### 3.1 Running the simulation

Run the following command:

```bash
python simulate_diffusion_video.py
```

The script generates simulated diffusion microscopy frames without requiring an input dataset.

The simulation parameters can be modified near the beginning of `simulate_diffusion_video.py`, including:

- `num_particles`: number of simulated particles
- `timesteps`: number of generated frames
- `diffusion_coefficient`: diffusion coefficient used in the simulation
- `image_size`: dimensions of each generated image
- `particle_intensity`: emission intensity of each particle

### 3.2 Expected output

The script creates a directory named `tiff_frames` containing 5,000 grayscale TIFF images:

```text
tiff_frames/
├── frame_0000.tiff
├── frame_0001.tiff
├── frame_0002.tiff
├── ...
└── frame_4999.tiff
```

Each output image is 128 × 128 pixels.

The expected runtime is approximately **[insert measured runtime]** on a computer with **[insert CPU, RAM, and operating system]**.

## 4. Reproduction Instructions

Videos 2–4 can be reproduced by changing the value of `diffusion_coefficient` in `simulate_diffusion_video.py` and running the script again:

```bash
python simulate_diffusion_video.py
```

Use the following parameter values:

| Output | `diffusion_coefficient` |
|---|---:|
| Video 2 | `[1/180]` |
| Video 3 | `[10/180]` |
| Video 4 | `[100/180]` |

The generated TIFF frames can subsequently be assembled into a video using an image-processing or video-editing program.

## 5. License

This project is licensed under the MIT License. See the `LICENSE` file for details.
