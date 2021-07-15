def parse_float(s):
    try:
        return float(s)
    except SyntaxError:
        return None
    except ValueError:
        return None
    except TypeError:
        return None
