T = int(input())
for i in range(T):
    (x, y) = map(int, input().split())
    a = int(x / 2)
    if x % 2 == 0:
        print(a * y)
    else:
        print((a + 1) * y)
