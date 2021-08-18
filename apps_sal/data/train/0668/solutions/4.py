t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [i for i in a] * k
    new = [0 for i in range(n * k)]
    new[0] = b[0]
    for i in range(n * k):
        new[i] = max([new[i - 1] + b[i], b[i]])
    print(max(new))
