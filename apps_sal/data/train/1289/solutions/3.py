t = eval(input())
i = 1
while(i <= t):
    j = eval(input())
    j = (2 * j) - 1
    k = 1
    p = 1
    while(k <= j):
        p = p * k
        k = k + 2
    print(p)
    print("\n")
    i = i + 1
