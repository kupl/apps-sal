def stairs(n):
    (c, r) = ('1 2 3 4 5 6 7 8 9 0'.split(), [])
    for i in range(n):
        temp = [c[j % 10] for j in range(i + 1)]
        r.append((' '.join(temp) + ' ' + ' '.join(temp[::-1])).rjust(n * 4 - 1))
    return '\n'.join(r)
