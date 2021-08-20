from re import findall


def denumerate(enum):
    enum = sorted(enum) if isinstance(enum, list) else ''
    if findall("(?<=\\[)(\\(\\d,\\s'[a-zA-Z\\d]'\\)[,\\s]*)*(?=\\])", str(enum)):
        (a, b) = zip(*enum)
        if all((a[i] == i for i in range(len(a)))):
            return ''.join(b)
    return False
