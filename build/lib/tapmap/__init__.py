"""TapMap: A generator for keyboard heatmap images."""

import argparse

from tapmap.processing import get_frequencies, blend_and_save

parser = argparse.ArgumentParser(
    description='Generate a keyboard heatmap from a text file.'
)
parser.add_argument(
    'input_filename', metavar='input_file', type=str,
    help='the name of the file to process'
)
parser.add_argument(
    'output_filename', metavar='output_file', type=str,
    help='the name of the image file to output'
)
parser.add_argument(
    '-d', type=int, help='dpi of the output image (defaults to 600)'
)
parser.add_argument(
    '-c', type=str, help='matplotlib cmap argument: '
    'https://matplotlib.org/users/colormaps.html (defaults to "viridis")'
)
args = parser.parse_args()


def main():
    """Entry point of "tapmap" terminal command."""
    filename = args.input_filename
    if filename is None:
        parser.error(
            'Please specify the filename of the text file to process.'
        )
    output_file = args.output_filename
    if output_file is None:
        parser.error(
            'Please specify the name of the image to generate.'
        )
    colormap = args.c
    if colormap is None:
        colormap = 'viridis'
    dpi = args.d
    if dpi is None:
        dpi = 600
    heatmap_data = get_frequencies(filename)
    blend_and_save(
        heatmap_data, output_file, colormap, dpi
    )
    print('Image generated: {}'.format(output_file))


if __name__ == '__main__':
    main()
