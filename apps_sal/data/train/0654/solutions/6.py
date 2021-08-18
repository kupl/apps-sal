t = int(input())
for i in range(0, t):
    x = []
    a, b, c = list(map(int, input().split()))
    x = [a, b, c]
    x = sorted(x)
    print(x[1])
