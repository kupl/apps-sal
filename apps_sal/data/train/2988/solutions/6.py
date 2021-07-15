def reverse_and_combine_text(text):
    t = text.split()    
    while len(t) > 1:
        t = [f'{a[::-1]}{b[::-1]}' for a, b in zip(*[iter([*t, ''])] * 2)]
    return t[0]
