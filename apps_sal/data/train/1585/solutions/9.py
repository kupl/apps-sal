T = int(input())
for i in range(T):
    (a, b) = map(int, input().split())
    print(max(a, b), max(a, b) + min(a, b))
