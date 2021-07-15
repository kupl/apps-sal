def parse_float(string):
    stuff = []
    blah = ''
    for i in string:
        if i in '0123456789.':
            stuff.append(i)
            blah = ''.join(stuff)
        else:
            return None
    return float(blah)
