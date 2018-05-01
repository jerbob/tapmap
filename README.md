TapMap
===================
Generate high-quality, customizable keyboard heatmaps with a single command.
- - - - 

# Installation: #
Use `python setup.py install` to install the package.

# Usage: #
`tapmap --help` will produce the following help message:
```
usage: tapmap [-h] [-d D] [-c C] input_file output_file

Generate a keyboard heatmap from a text file.

positional arguments:
  input_file   the name of the file to process
  output_file  the name of the .png file to output

optional arguments:
  -h, --help   show this help message and exit
  -d D         dpi of the output image (defaults to 600)
  -c C         matplotlib cmap argument:
               https://matplotlib.org/users/colormaps.html (defaults to
               "viridis")
```
To generate a keyboard heatmap `map.png` from an input file `input.txt`, use: `tapmap input.txt map.png`
TapMap also supports all matplotlib colormaps: `tapmap input.txt map.png -c plasma`