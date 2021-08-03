for _ in range(eval(input())):
    n = eval(input())
    l = list(map(int, input().split()))
    c = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for m in range(n):
                    a = set(l[i:j + 1])
                    b = set(l[k:m + 1])
                    if len(a) and len(b) and len(a & b) == 0:
                        c += 1
    print(c / 2)
