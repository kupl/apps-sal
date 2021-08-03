for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    for i in range(len(l)):
        if i == 0:
            c += 1
        else:
            if i >= 5:
                t_1 = min(l[i - 5:i])
            else:
                t_1 = min(l[:i])
            if l[i] < t_1:
                c += 1
    print(c)
