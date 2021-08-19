def morse_converter(s):
    return int(''.join((str(9 - '----.....-----'.rindex(s[i:i + 5])) for i in range(0, len(s), 5))))
