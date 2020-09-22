"""
Imports and display rectangle data from different file formats on stdout

Usage:
    app.py --type=<type> IN_FILE

Arguments:
    IN_FILE     Input CAD file

Options:
  -t --type=<type>     The originating CAD program that created the file (has to be quadium or rect_star)
  -h --help            Show this screen.
"""
from docopt import docopt
from rectangles import Quadium, RectStar
import json

""" WARNING! Do not change the command-line interface of the application """

if __name__ == '__main__':
    arguments = docopt(__doc__)
    file_type = arguments.get('--type')
    if file_type == 'quadium':
        cad_file_parser = Quadium.from_file
    elif file_type == 'rect_star':
        cad_file_parser = RectStar.from_file
    else:
        raise RuntimeError('Invalid CAD file type')
    cad = cad_file_parser(arguments['IN_FILE'])
    print(json.dumps(cad.to_dict(), indent=2))
