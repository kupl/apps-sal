def parse_float(string):
    try:
        x = float(string)
        return x
    except ValueError:
        return None
    except TypeError:
        try:
            y = float(''.join(string))
            return y
        except ValueError:
            return None
        

            


