try:
    t = int(input().strip())
    for abc in range(t):
        n = list(input().strip())
        if n == []:
            n = list(input().strip())
        for i in range(len(n)):
            if int(n[i]) == 1:
                n[i] = '0'
            else:
                n[i] = int(n[i]) - 2
        for i in n:
            print(i, end='')
        print('\n')
except Exception:
    pass
