def decrypt(s):
    (count_each, li) = ([[s.count(i), i] for i in set(s) if i.isalpha() and i.islower()], ['0'] * 26)
    for i in count_each:
        li[ord(i[1]) - 97] = repr(i[0])
    return ''.join(li)
