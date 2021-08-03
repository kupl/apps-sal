def to_bits(string):
    a = list(string)
    words = [w.replace('\n', ' ') for w in a]
    b = ''.join(words)
    lst = b.split(' ')
    lst2 = []
    for x in lst:
        if x.isdigit():
            lst2.append(x)
#     print(lst2)
    lst3 = [int(i) for i in lst2]
    lst3.sort()
    max(lst3)
    print(len(lst3))
    print((lst3))
    a = []
    for x in range(5000):
        a.append(0)
    len(a)
    for i in range(len(lst3)):
        a[lst3[i]] = 1
    print(sum(a))
    return a
