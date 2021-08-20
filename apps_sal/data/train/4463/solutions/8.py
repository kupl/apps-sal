def alphabet_position(text):
    upper_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower_alpha = 'abcdefghijklmnopqrstuvwxyz'
    l = []
    for i in text:
        if i in upper_alpha:
            index = upper_alpha.index(i) + 1
            l.append(str(index))
        elif i in lower_alpha:
            index = lower_alpha.index(i) + 1
            l.append(str(index))
    return ' '.join(l)
