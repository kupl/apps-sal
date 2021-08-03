# the obvious approach...
def parse_float(string):
    try:
        return float(string)
    except ValueError:
        return None

# hand rolled


def parse_float(string):
    try:
        whole, fractional = string.split(".", maxsplit=1)
    except:
        return None

    if not all(d.isdigit() for d in whole) or \
       not all(d.isdigit() for d in fractional):
        return None

    whole = sum(int(val) * 10**place for place, val in enumerate(whole[::-1]))
    fractional = sum(int(val) * 10**-(place + 1) for place, val in enumerate(fractional))

    return whole + fractional
