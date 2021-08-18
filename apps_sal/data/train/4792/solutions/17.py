from re import findall


def parse_float(string):
    if isinstance(string, str) and findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', string):
        return float(string)
