def morse_converter(string):
    dict = {tuple(a): str(c) for (c, a) in enumerate(['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.'])}
    return int(''.join(map(dict.get, zip(*[iter(string)] * 5))))
