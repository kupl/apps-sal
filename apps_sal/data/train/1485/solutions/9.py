t = int(input())
for _ in range(t):
    n = int(input())
    lr = [0] * n
    for i in range(n):
        s = input()
        lr[i] = s[:n // 2].count("1") - s[n // 2:].count("1")
    lrsum = sum(lr)

    if(lrsum == 0):
        print("0")

    else:
        x = [abs(lrsum - 2 * lr[i]) for i in range(n)]
        print(min(x))
