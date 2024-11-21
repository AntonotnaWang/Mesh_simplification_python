import pyvista as pv
from pyvista import examples
import imageio
import numpy as np

# Load a sample mesh or your own 3D object file
mesh = pv.read("dinosaur_simp_10_1.obj")
# mesh = examples.download_st_helens().warp_by_scalar()

# Set up the plotter
plotter = pv.Plotter(off_screen=True)
plotter.add_mesh(mesh)

# Set the radius of the sphere (distance from the object)
radius = 216

# Set the focal point (center of the object)
focal_point = (0, 0, 0)

# Create a list to store frames
frames = []

# Number of frames for a full rotation
n_frames = 72

# Rotate the object and capture frames
for i in range(n_frames):
    angle = 2 * np.pi * i / n_frames  # Current angle in radians
    # Calculate camera position on the sphere
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    z = radius * 0.1  # Slight elevation to view from above
    plotter.camera_position = [(x, y, z), focal_point, (0, 0, 1)]  # (position, focal point, up direction)
    plotter.render()  # Render the current frame
    # Capture the current frame
    image = plotter.screenshot()
    frames.append(image)

# Close the plotter
plotter.close()

# Save frames as a GIF
imageio.mimsave('rotating_object.gif', frames, fps=10)
