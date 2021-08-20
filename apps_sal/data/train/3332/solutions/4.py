def autocorrect(s):
    (s, n) = (s.split(), [])
    for i in s:
        if i == 'you' or i == 'u':
            n.append('your sister')
        elif len(i) == 4 and i[:-1] == 'you':
            n.append('your sister' + i[-1])
        elif i.count('Y') + i.count('y') + i.count('o') + i.count('u') == len(i) and i.count('u') == len(i) - 2:
            n.append('your sister')
        else:
            n.append(i)
    return ' '.join(n)
