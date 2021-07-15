def unusual_sort(array):
    return sorted(array, key=lambda x: (str(x).isdigit(), str(x), -isinstance(x, int)))
