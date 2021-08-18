for _ in range(int(input())):
    t, k = input().split()
    k = int(k)
    str = ''
    for c in range(97, 123):
        if chr(c) in t:
            if k > 0:
                str += chr(c)
                k = k - 1
            else:
                continue
        else:
            str += chr(c)
    if len(str) >= len(t):
        print(str[:len(t)])
    else:
        print('NOPE')
