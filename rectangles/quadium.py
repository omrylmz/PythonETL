from .common import BaseRectanglesFile, ParseError
import math
import xml.etree.ElementTree as ET


class Quadium(BaseRectanglesFile):
    """ Quadium decoder """

    def to_dict(self):
        """ Outputs a dictionary from the CAD file data """
        for rect in self.rectangles:
            [px, py] = rect["point"]
            w = rect["width"]
            h = rect["height"]
            r = math.radians(rect["rotation"])
            px = px - (w * 0.5 * math.cos(r)) + (h * 0.5 * math.sin(r))
            py = py + (w * 0.5 * math.sin(r)) + (h * 0.5 * math.cos(r))
            rect["point"] = [round(px, 1), round(py, 1)]
        return {"bg": self.bg, "rectangles": self.rectangles}

    @classmethod
    def _parse_input_data(cls, data: str):
        quad = Quadium()
        root = ET.fromstring(data)
        quad.bg = root.find("background").get("color", default="#FFFFFF")

        # Order of the rectangles/squares may be important
        # Otherwise, we could directly find the list of squares with 'root.findall("./drawing/square")'
        for child in root.find("drawing"):
            if child.tag == "square":
                quad.rectangles.append({
                    "point": [
                        float(child.find("center").get("x", default="0")),
                        float(child.find("center").get("y", default="0"))
                    ],
                    "width": float(child.find("dimension").text),
                    "height": float(child.find("dimension").text),
                    "rotation": int(child.get("rotate", default="0deg")[:-3]),
                    "color": child.get("color", default="#FFFFFF")
                })

            elif child.tag == "rectangle":
                quad.rectangles.append({
                    "point": [
                        float(child.find("center").get("x", default="0")),
                        float(child.find("center").get("y", default="0"))
                    ],
                    "width": float(child.find("width").text),
                    "height": float(child.find("height").text),
                    "rotation": int(child.get("rotate", default="0deg")[:-3]),
                    "color": child.get("color", default="#FFFFFF")                  
                })
            else:
                raise ParseError("XML file is broken.")

        return quad