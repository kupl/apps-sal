try:
    for i in range(int(input())):
        n = int(input())
        b = input()
        b = b.split()
        b = list(map(int, b))
        day = 0
        t = list(map(int, b))
        t[0] = -1
        tell = b[0]
        known = 1
        q = [-1 for i in range(n)]
        for i in range(1, n):
            if t[i] != -1:
                p = 0
                c = 0
                if tell > n - known:
                    for j in range(i, n):
                        t[j] = -1
                        known += 1
                        p += 1
                        c += b[j]
                    day += 1
                    tell += c
                else:
                    for j in range(i, i + tell):
                        t[j] = -1
                        known += 1
                        p += 1
                        c += b[j]
                    day += 1
                    tell += c
                if t == q:
                    break
        print(day)

except:
    None
