d = {j: i for (i, j) in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')}


def base64_to_base10(s):
    return sum((d[j] * 64 ** (len(s) - 1 - i) for (i, j) in enumerate(s)))
