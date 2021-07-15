def base64_to_base10(s):
    n = 0
    for c in s:
        n = n * 64 + 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'.index(c)
    return n
