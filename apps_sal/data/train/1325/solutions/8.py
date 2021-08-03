t = int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    print(int((a + b + c) / 2 - b), end=" ")
    print(int((a + b + c) / 2 - c), end=" ")
    print(int((a + b + c) / 2 - a))
    print()
