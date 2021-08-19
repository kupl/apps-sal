for _ in range(int(input())):
    s = input()
    s = list(s)
    for (n, i) in enumerate(s):
        if i in 'aeiou':
            s[n] = 1
        else:
            s[n] = 0
    print(int(''.join(map(str, s)), 2))
