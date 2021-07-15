def convert_num(number, base):
    try:
        return {'bin': bin, 'hex': hex}[str(base)](number)
    except KeyError:
        return 'Invalid base input'
    except TypeError:
        return 'Invalid number input'
