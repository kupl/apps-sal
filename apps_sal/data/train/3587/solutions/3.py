def original_number(s):
    (r, s) = ([], list(s))
    for (word, n) in [('ZERO', 0), ('WTO', 2), ('XSI', 6), ('GEIHT', 8), ('THREE', 3), ('UFOR', 4), ('ONE', 1), ('FIVE', 5), ('VSEEN', 7), ('NINE', 9)]:
        while word[0] in s:
            for c in word:
                s.remove(c)
            r.append(n)
    return ''.join((str(e) for e in sorted(r)))
