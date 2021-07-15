SPECIAL = "-',."

def scramble_words(words):
    output = []
    for word in words.split():
        sortable = [c for c in word if c.isalpha()]
        typgly = sortable[:1] + sorted(sortable[1:-1]) + sortable[-1:]
        output.append(''.join(c if not c.isalpha() else typgly.pop(0) for c in word))
    return ' '.join(output)
