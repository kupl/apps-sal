# https://habrastorage.org/webt/xt/af/nj/xtafnjpq-xw3lu0aisu68q22elg.png
from re import findall

def parse_float(string):
    if isinstance(string, str) and findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', string):
        return float(string)
