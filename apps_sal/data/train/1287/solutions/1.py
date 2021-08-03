for _ in range(int(input())):
    s = input()
    ss = list(s)
    for n, i in enumerate(ss):
        if i in 'aeiou':
            ss[n] = 1
        else:
            ss[n] = 0
    print(int(''.join(map(str, ss)), 2))
