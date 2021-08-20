def decipher(cipher):
    (lst, it) = ([], iter(cipher))
    for c in it:
        lst.append(chr(int(''.join((c, next(it), next(it)) if c == '1' else (c, next(it))))))
    return ''.join(lst)
