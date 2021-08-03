t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    s = [l[0]]
    for i in range(0, n - 1):
        s.append(s[i] ^ l[i + 1])
    print(s[-1])
