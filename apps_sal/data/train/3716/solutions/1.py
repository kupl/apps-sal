def unusual_sort(array):
    return sorted(array, key=lambda item: (str(item).isdigit(), str(item), isinstance(item, str)))
