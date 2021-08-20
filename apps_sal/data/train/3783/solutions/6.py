def frame(text, char):
    width = max([len(x) for x in text]) + 4
    a = '\n'.join([char + ' ' + x + ' ' * (width - len(x) - 3) + char for x in text])
    return f'{char * width}\n{a}\n{char * width}'
