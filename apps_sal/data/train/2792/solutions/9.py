def unusual_lex_order(arr):
    ans = [s[::-1] for s in arr]
    ans.sort()
    return [s[::-1] for s in ans]
