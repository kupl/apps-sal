def unusual_lex_order(arr):
    return sorted(arr, key=lambda x: x[::-1])
