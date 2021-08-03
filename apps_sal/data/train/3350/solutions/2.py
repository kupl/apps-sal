def hex_string_to_RGB(s):
    return {c: int(s[1 + 2 * i:3 + 2 * i], 16) for i, c in enumerate('rgb')}
