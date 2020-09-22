class BaseRectanglesFile(object):
    def __init__(self):
        self.rectangles = []
        self.bg = '#FFF'

    def to_dict(self):
        """ Outputs a dictionary from the CAD file data """
        raise NotImplementedError()

    @classmethod
    def from_file(cls, filename: str) -> 'BaseRectanglesFile':
        """ Static factory that creates an object from a CAD file """
        with open(filename) as fp:
            return cls._parse_input_data(fp.read())

    @classmethod
    def _parse_input_data(cls, data: str):
        raise NotImplementedError()


class ParseError(Exception):
    def __init__(self, str):
        self.msg = str
    
    def message(self):
        print("Parsing error occurred:", self.msg)