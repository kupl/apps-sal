def unusual_lex_order(lst):
    return sorted(lst, key=lambda x: x[::-1])
