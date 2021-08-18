for _ in range(int(input())):
    n = list(input())
    if len(n) % 2 == 1:
        print(-1)
    else:
        s1 = n.count('0')
        s2 = n.count('1')
        if s1 > 0 and s2 > 0:
            print(abs(s1 - s2) // 2)
        else:
            print(-1)
