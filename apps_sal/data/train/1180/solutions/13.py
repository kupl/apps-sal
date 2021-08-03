try:
    T = int(input())
    for i in range(T):
        N, K, x, y = map(int, input().split())
        c = 0
        a = K % 4
        if a == 0:
            a = 4
        if x > y:
            c = 1
        l = [0, N]
        for j in range(a):
            if c == 1:
                if x in l and y in l:
                    break
                elif x == N or x == 0:
                    x, y = y, x
                elif y == N or y == 0:
                    b = y
                    y = N - x
                    x = N - b
                else:
                    b = N - x
                    x += b
                    y += b
            else:
                if x in l and y in l:
                    break
                elif y == N or y == 0:
                    x, y = y, x
                elif x == N or x == 0:
                    b = x
                    x = N - y
                    y = N - b
                else:
                    b = N - y
                    x += b
                    y += b
        print(x, y)
except EOFError:
    pass
