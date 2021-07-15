def base64_to_base10(str):
    res = 0
    for c in str:
        res *= 64
        res += "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".find(c)
    return res

