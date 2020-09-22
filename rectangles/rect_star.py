from .common import BaseRectanglesFile, ParseError
import re


class RectStar(BaseRectanglesFile):
    """ RectStar Decoder """

    def to_dict(self):
        """ Outputs a dictionary from the CAD file data """
        return {"bg": self.bg, "rectangles": self.rectangles}

    @classmethod
    def _parse_input_data(cls, data: str):
        rstar = RectStar()
        data_lst = data.split()
        data_itr = iter(data_lst)

        # # We could easily find the solution using regexes, but we will use a more robust way.
        # recstar_rgx = re.compile(r"\.RECTSTAR\s*\{\s*(file)\s*(\w*\.rstar)\s*(bg)\s*(\#\w*)\s*\}")
        # m = re.match(recstar_rgx, data)
        # bg = m.group(4)
        # print(bg)
        #
        # # Or even better use the string with known space characters \n \r \r\n .
        # data_str = " ".join(data_lst)
        # recstar_rgx = re.compile(r"\.RECTSTAR\s\{\s(file)\s(\w*\.rstar)\s(bg)\s(\#\w*)\s\}")
        # m = re.match(recstar_rgx, data_str)
        # bg = m.group(4)
        # print(bg)
        #
        # # A similar thing could be done for .RECT files first finding the list of .RECT matches with findall()

        try:
            try:
                assert(".RECTSTAR" == next(data_itr)), r'".RECTSTAR" was expected.'
                assert("{" == next(data_itr)), r'{ was expected'
                assert("file" == next(data_itr)), r'"file" was expected.'
                next(data_itr)
                assert("bg" == next(data_itr)), r'"bg" was expected.'
                rstar.bg = next(data_itr)
                assert("}" == next(data_itr)), r'"}" was expected.'
            except AssertionError as error:
                raise ParseError(error)
        except ParseError as parse_error:
            parse_error.message()

        data_str = next(data_itr)
        while ".RECT" == data_str:
            # # If the format order is strongly specified, the following is more efficient.
            # # All '{' and '}' letters could be deleted. They are left for better assertion check.
            # assert("{" == next(data_itr))
            # assert("pt" == next(data_itr))
            # ptx = next(data_itr)
            # pty = next(data_itr)
            # assert("w" == next(data_itr))
            # w = next(data_itr)
            # assert("h" == next(data_itr))
            # h = next(data_itr)
            # assert("rot" == next(data_itr))
            # rot = next(data_itr)
            # assert("color" == next(data_itr))
            # color = next(data_itr)
            # assert("}" == next(data_itr))

            assert("{" == next(data_itr))
            data_str = next(data_itr)
            while "}" != data_str:
                if "pt" == data_str:
                    ptx = next(data_itr)
                    pty = next(data_itr)
                elif "w" == data_str:
                    w = next(data_itr)
                elif "h" == data_str:
                    h = next(data_itr)
                elif "rot" == data_str:
                    rot = next(data_itr)
                else:
                    color = next(data_itr)
                data_str = next(data_itr)
            
            rstar.rectangles.append({
                "point": [float(ptx[1:-1]), float(pty[:-1])],
                "width": float(w),
                "height": float(h),
                "rotation": int(rot),
                "color": color
            })

            try :
                data_str = next(data_itr)
            except StopIteration as e:
                print(e)
                break
        return rstar