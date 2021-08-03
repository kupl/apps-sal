def convert(n):
    return ''.join([chr(int(n[i:i + 2])) for i in range(0, len(n) - 1, 2)])
