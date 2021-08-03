def merge_arrays(first, second):
    nowa = first + second
    nowa = list(set(nowa))
    nowa.sort()
    return nowa
