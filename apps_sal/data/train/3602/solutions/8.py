from re import findall


def run_length_encoding(string):
    return [[len(a), b] for (a, b) in findall('((.)\\2*)', string)]
