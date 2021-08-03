t = int(input())
for foo in range(t):
    n = int(input())
    t = list(map(int, input().split()))
    same = 1
    pair = 0
    for i in range(n):
        if t[i] == t[i - 1]:
            pair = 1
        else:
            same = 0
    if same == 1:
        print(1)
        print(*([1] * n))
    else:
        if n % 2 == 0:
            print(2)
            print(*([1, 2] * (n // 2)))
        else:
            if pair == 1:
                print(2)
                s = [1] * n
                p = 0
                for i in range(n - 1):
                    if p == 1 or t[i] != t[i - 1]:
                        s[i] = 3 - s[i - 1]
                    else:
                        p = 1
                        s[i] = s[i - 1]
                print(*s)
            if pair == 0:
                print(3)
                print(*([1, 2] * (n // 2)), 3)
