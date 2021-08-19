def find_missing_letter(c):
    return next((chr(ord(c[i]) + 1) for i in range(len(c) - 1) if ord(c[i]) + 1 != ord(c[i + 1])))
