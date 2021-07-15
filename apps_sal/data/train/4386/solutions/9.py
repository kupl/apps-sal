def is_in_middle(s):
    return 'abc' in [s[len(s) // 2 - 1: len(s) // 2 + 2] if len(s) % 2 else s[len(s) // 2 - 2: len(s) // 2 + 2]][0]
