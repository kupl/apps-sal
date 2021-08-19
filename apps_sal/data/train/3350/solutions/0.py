def hex_string_to_RGB(s):
    return {i: int(s[j:j + 2], 16) for (i, j) in zip('rgb', [1, 3, 5])}
