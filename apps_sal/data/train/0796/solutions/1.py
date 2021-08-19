def f(x, y):
    if x < 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 1
    else:
        return 0


for _ in range(eval(input())):
    n = eval(input())
    c = 1
    b = []
    a = list(map(int, input().split()))
    if n == 1:
        print(1)
        continue
    for i in range(n - 1):
        if a[i] * a[i + 1] < 0:
            c += 1
        else:
            for j in range(c):
                b.append(c - j)
            c = 1
    for j in range(c):
        b.append(c - j)
    print(' '.join(map(str, b)))
