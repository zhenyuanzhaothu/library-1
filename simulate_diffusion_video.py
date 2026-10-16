import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

# Set particle parameters
num_particles = 50  # Number of particles #
timesteps = 5000  # Number of time steps #
diffusion_coefficient = 1/18  # Diffusion coefficient 10^-14 m2s-1 set by Gaussian Model with 60 nm pixel size and 20 ms time step
image_size = (128, 128)  # Image dimensions (pixels) #
particle_intensity = 255  # Particle emission intensity #

# Create a directory for storing frames
output_dir = 'tiff_frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize particle positions and the background
particles = np.random.uniform(0, image_size[0], (num_particles, 2))  # Initialize particle positions
background_intensity = 30  # Background noise intensity

# Generate a 7×7 Gaussian kernel to simulate a diffraction-limited spot
def generate_particle_kernel(size=7, sigma=1.0):
    """Generate a Gaussian kernel to simulate an optical microscope's point spread function (PSF)."""
    ax = np.linspace(-(size - 1) / 2., (size - 1) / 2., size)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)  # Normalize

particle_kernel = generate_particle_kernel(size=7, sigma=1.0)  # 7×7 Gaussian blur kernel

# Improved particle motion function
def update_particles():
    """Update particle positions based on the diffusion coefficient (consistent with physical laws)."""
    global particles
    # Calculate the step size (proportional to the square root of the diffusion coefficient and time)
    step_size = np.sqrt(2 * diffusion_coefficient)  # Step size per unit time
    # Generate random directions (uniformly distributed in the two-dimensional plane)
    directions = np.random.uniform(-1, 1, (num_particles, 2))
    directions /= np.linalg.norm(directions, axis=1, keepdims=True)  # Normalize
    # Update particle positions (vectorized for improved performance)
    particles += step_size * directions

# Generate all frames and save them as TIFF files
for frame_num in range(timesteps):
    # Create an image with background noise
    frame = np.random.normal(loc=background_intensity, scale=5, size=image_size)
    
    # Update particle positions
    update_particles()
    
    # Apply boundary conditions (reflecting boundary conditions)
    particles[:, 0] = np.mod(particles[:, 0], image_size[0] - 1)
    particles[:, 1] = np.mod(particles[:, 1], image_size[1] - 1)
    
    # Apply the Gaussian kernel at each particle position
    for particle in particles:
        x, y = int(particle[0]), int(particle[1])
        # Prevent indices from going out of bounds
        x = max(3, min(x, image_size[0] - 4))
        y = max(3, min(y, image_size[1] - 4))
        frame[x-3:x+4, y-3:y+4] += particle_kernel * particle_intensity
    
    # Ensure that the image signal intensity remains within the valid range
    frame = np.clip(frame, 0, 255)
    
    # Save as a TIFF image
    filename = f"{output_dir}/frame_{frame_num:04d}.tiff"
    im = Image.fromarray(np.uint8(frame), mode='L')  # Grayscale mode 'L'
    im.save(filename)
