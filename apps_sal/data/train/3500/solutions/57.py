def remove_exclamation_marks(s):
    s = s.split(' ')
    no_marks = []
    for char in s:
        char = list(char)
        no_exc = []
        for x in char:
            if x != '!':
                no_exc.append(x)
        collect = ''.join(no_exc)
        no_marks.append(collect)
    return ' '.join(no_marks)
