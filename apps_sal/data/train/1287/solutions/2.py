for _ in range(int(input())):
    a = input()
    b = []
    for i in a:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            b.append(1)
        else:
            b.append(0)
    c = 0
    l = len(a)
    for i in range(l):
        if b[-i - 1]:
            c += 1 << i
    print(c)
