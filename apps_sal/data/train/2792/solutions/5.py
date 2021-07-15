def unusual_lex_order(strings):
    return sorted(strings, key=lambda s: s[::-1])
