def frame(lines, char):
    l = len(max(lines, key=len))
    row = char * (l + 4)
    body = '\n'.join((f'{char} {line:<{l}s} {char}' for line in lines))
    return f'{row}\n{body}\n{row}'
