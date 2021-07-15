def tv_remote(word):
    l = ['abcde123',
         'fghij456',
         'klmno789',
         'pqrst.@0',
         'uvwxyz_/',]
    a, b, s = 0, 0, 0
    for i, m in enumerate(word):
        for j, n in enumerate(l):
            if m in n:
                a1 = j
                b1 = n.index(m)
                s += abs(a-a1) + abs(b-b1) + 1
                break
        a, b = a1, b1
    return s

