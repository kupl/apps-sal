t = int(input())
for x in range(t):
    (a, b) = map(int, input().split())
    if a > b:
        print(a, a + b)
    else:
        print(b, a + b)
