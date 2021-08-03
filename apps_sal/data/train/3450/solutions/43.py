def array(string):
    elems = list(map(str.strip, string.split(',')))

    if len(elems) < 3:
        return None

    return ' '.join(elems[1:-1])
