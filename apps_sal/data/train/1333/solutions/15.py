m = pow(10, 9) + 7
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    t = 1
    y = 0
    for i in range(n - 1):
        if l[i] <= l[i + 1] and l[i] & l[i + 1] == l[i]:
            y = y + bin(l[i]).count('1')
        else:
            t = 0
            break
    t = t * pow(2, y, m) % m
    print(t % m)
