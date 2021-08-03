def convert(number):
    return ''.join(chr(int(number[a:a + 2])) for a in range(0, len(number), 2))
