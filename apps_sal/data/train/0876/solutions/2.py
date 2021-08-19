# cook your dish here
t = int(input())
for _ in range(t):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    x = max(A)
    y = min(A)
    # print(x)
    if (x - y) < X:
        print("YES")
    else:
        print("NO")
