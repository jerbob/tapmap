"""Main Image and Data Processing functions."""

import os
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image, ImageChops

from tapmap.char_map import get_coords, get_all_pixels

# Get full path of module's directory
dir_path = os.path.dirname(os.path.realpath(__file__))

# Make entire array visible when printing data
np.set_printoptions(threshold=np.nan)

# Open the keyboard image for later use
keyboard = Image.open(
    '{}/images/keyboard.png'.format(dir_path)
)


def get_frequencies(filename):
    """Get the frequencies of certain keypresses."""
    print('Processing file {}...'.format(filename))
    pixels = []
    heatmap_data = np.asarray([[0] * 57] * 21)
    # Open the given file and read the contents
    with open(filename) as file:
        contents = file.read()
    # Get the pixels covered by each character, and append these to pixels
    for char in contents:
        coords = get_coords(char)
        if coords:
            for coord in coords:
                pixels.append(coord)
    # Increment the appropriate coordinate for each pixel covered
    for coordinate in pixels:
        x, y = coordinate
        heatmap_data[x][y] += 1
    # Get the sum of all data, and divide all values by that sum
    total = np.sum(heatmap_data)
    heatmap_data = heatmap_data / total
    # Get the values for the shift key, and scale them down by 70%
    for pixel in get_all_pixels(((18, 18), (19, 34))):
        x, y = pixel
        heatmap_data[x][y] *= 0.3
    print('Finished processing file {}.'.format(filename))
    # Return the final array
    return heatmap_data


def blend_and_save(heatmap_data, filename, colormap, dots):
    """Plot a heatmap, upscale it to the keyboard and save a blended image."""
    print('Generating heatmap...')
    # Clear the heatmap plot and axes
    plt.clf()
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')
    # Display the data on the heatmap
    plt.imshow(
        heatmap_data, interpolation='lanczos', zorder=1, cmap=colormap
    )
    # Save the heatmap plot
    plt.savefig(
        '{}/images/heatmap.png'.format(dir_path),
        dpi=dots,
        pad_inches=0,
        transparent=True,
        bbox_inches='tight'
    )
    print('Blending and saving image...')
    # Open the heatmap image
    heatmap = Image.open(
        '{}/images/heatmap.png'.format(dir_path)
    )
    # Resize the heatmap to the keyboard's size, with antialiasing
    heatmap = heatmap.resize(keyboard.size, Image.ANTIALIAS)
    heatmap.save(
        '{}/images/heatmap.png'.format(dir_path)
    )
    # Blend the images, and save
    blended = ImageChops.darker(keyboard, heatmap)
    blended.save(
        '{0}/{1}'.format(os.getcwd(), filename)
    )
