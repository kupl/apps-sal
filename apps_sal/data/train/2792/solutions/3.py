def unusual_lex_order(arr):
    return sorted(arr, key=lambda word: word[::-1])
