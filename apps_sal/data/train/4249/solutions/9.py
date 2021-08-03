def base64_to_base10(str):
    return sum('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'.index(n) * 64**i for i, n in enumerate(str[::-1]))
