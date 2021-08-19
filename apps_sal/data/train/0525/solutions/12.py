t = int(input())
for _ in range(t):
    (a, b, c) = input().split()
    (a, b, c) = (int(a), int(b), int(c))
    d = c - c % a + b
    if d > c:
        print(d - a)
    else:
        print(d)
