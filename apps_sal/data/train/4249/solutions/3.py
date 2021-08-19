def base64_to_base10(s):
    return 0 if len(s) == 0 else 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'.index(s[-1]) + 64 * base64_to_base10(s[:-1])
