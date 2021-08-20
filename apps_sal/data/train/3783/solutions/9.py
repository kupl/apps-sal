def frame(text, char):
    w = max(map(len, text))

    def f():
        yield (char * (w + 4))
        for line in text:
            yield f'{char} {line:<{w}} {char}'
        yield (char * (w + 4))
    return '\n'.join(f())
