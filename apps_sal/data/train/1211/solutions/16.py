for t in range(int(input())):
    a = input()
    s = ''
    for i in a:
        s += i
        if i == 'c':
            if 'abc' in s:
                s = s[:len(s) - 3]
    print(s)
