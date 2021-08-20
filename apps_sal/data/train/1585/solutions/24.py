N = int(input())
for i in range(N):
    (a, b) = list(map(int, input().split()))
    if a > b:
        print(a, a + b)
    elif a < b:
        print(b, a + b)
