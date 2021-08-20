n = int(input())
for i in range(0, n):
    (a, b) = list(map(int, input().split()))
    c = a + b
    n = 1
    while True:
        s = c + n
        for j in range(2, s):
            if s % j == 0:
                break
        else:
            break
        n += 1
    print(n)
