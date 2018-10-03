TapMap
===================

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/43ab4be7f3f541daa98be9a4709efc9a)](https://app.codacy.com/app/AnonGuy/TapMap?utm_source=github.com&utm_medium=referral&utm_content=AnonGuy/TapMap&utm_campaign=Badge_Grade_Dashboard) [![Updates](https://pyup.io/repos/github/AnonGuy/TapMap/shield.svg)](https://pyup.io/repos/github/AnonGuy/TapMap/)


Generate high-quality, customizable keyboard heatmaps with a single command.
- - - - 

# Installation: #
Use `pip install tapmap` to install the package.

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
To generate a keyboard heatmap `map.png` from an input file `input.txt`, use: `tapmap input.txt map.png` <br/>


![Default CMap](https://i.imgur.com/VfxQECB.png)

TapMap also supports all matplotlib colormaps: `tapmap input.txt map.png -c winter`

![Winter CMap](https://i.imgur.com/PcIljzp.png)

There are 79 colormaps to choose from, take your pick from [the matplotlib reference.](https://matplotlib.org/users/colormaps.html)
