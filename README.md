1. System requirements
Python 3.10 or later
Required Python packages:
- numpy
- matplotlib
- Pillow

Tested operating system:
- Windows 11

No non-standard hardware or GPU is required.

2. Installation guide
'''
git clone https://github.com/zhenyuanzhaothu/library-1.git
cd library-1
python -m venv .venv
pip install numpy pillow
'''
Typical installation time: very fast on a standard desktop computer with an existing Python installation.

3. Demo
3.1 Instructions to run on data:
'''
python simulate_diffusion_video.py
'''
The script generates simulated diffusion microscopy frames without requiring an input dataset.

3.2 Expected output:
The script creates a directory named `tiff_frames` containing 5,000 grayscale TIFF images named `frame_0000.tiff` through `frame_4999.tiff`. Each image is 128 × 128 pixels.

3.3 Reproduction instructions:
To reproduce video2-4, change the diffusion_coefficient values supplied in `simulate_diffusion_video.py` and run.
