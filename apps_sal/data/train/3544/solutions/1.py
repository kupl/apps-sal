def morse_converter(s):
    it = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
    return int(''.join(str(it.index(s[i:i+5])) for i in range(0, len(s), 5)))
