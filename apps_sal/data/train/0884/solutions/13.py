for _ in range(int(input())):
    (x, k) = map(int, input().split(' '))
    s = 0
    for i in range(2, x + 1):
        if x % i == 0:
            s += i ** k
    s1 = 0
    for i in range(2, k + 1):
        if k % i == 0:
            s1 += i * x
    print(s, s1)
