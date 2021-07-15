tbl = {
    x: str(i % 10)
    for i, x in enumerate(['.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----'], 1)
}

def morse_converter(s):
    return int(''.join(tbl[s[i:i+5]] for i in range(0, len(s), 5)))
