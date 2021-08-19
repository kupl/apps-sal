for j in range(int(input())):
    a = input()
    x = list(a)
    n = len(x)
    am = 0
    if n % 2 == 0:
        for i in range(n):
            if x[i] == '.' or x[n - i - 1] == '.':
                if x[i] == '.' and x[n - i - 1] != '.':
                    x[i] = x[n - i - 1]
                elif x[n - i - 1] == '.' and x[i] != '.':
                    x[n - i - 1] = x[i]
                else:
                    x[i] = 'a'
                    x[n - i - 1] = 'a'
            elif x[i] != x[n - i - 1]:
                am = 1
                break
    else:
        b = n // 2
        for i in range(n):
            if b == i:
                if x[i] == '.':
                    x[i] = 'a'
                else:
                    continue
            elif x[i] == '.' or x[n - i - 1] == '.':
                if x[i] == '.' and x[n - i - 1] != '.':
                    x[i] = x[n - i - 1]
                elif x[n - i - 1] == '.' and x[i] != '.':
                    x[n - i - 1] = x[i]
                else:
                    x[i] = 'a'
                    x[n - i - 1] = 'a'
            elif x[i] != x[n - i - 1]:
                am = 1
                break
    if am == 0:
        print(''.join(x))
    else:
        print(-1)
