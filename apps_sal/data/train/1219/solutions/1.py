t = int(input())
for _ in range(t):
    nm = list(map(int, input().split()))
    if nm[0] == 1 or nm[1] == 1:
        print(1)
    else:
        k = nm[0] // 2
        print(pow(nm[1], k * (k + 1), 10 ** 9 + 7))
