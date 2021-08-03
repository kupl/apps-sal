t = eval(input())
for i in range(t):
    big = [0, 0]
    n = eval(input())
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    for k in range(n):
        if a[k] * b[k] > big[0]:
            big[0] = a[k] * b[k]
            big[1] = b[k]
            c = k + 1
        elif a[k] * b[k] == big[0]:
            if big[1] < b[k]:
                c = k + 1
                big[1] = b[k]
    print(c)
