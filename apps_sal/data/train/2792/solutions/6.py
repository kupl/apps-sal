def unusual_lex_order(arr):
    return sorted(arr, key=lambda item: item[-1]) if all((len(x) == 1 for x in arr)) else sorted(arr, key=lambda item: (item[-1], item[-2])) if any((len(x) == 2 for x in arr)) else sorted(arr, key=lambda item: (item[-1], item[-2], item[-3]))
