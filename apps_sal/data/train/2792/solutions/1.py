def unusual_lex_order(arr):
    return sorted(arr, key=lambda s: s[::-1])
