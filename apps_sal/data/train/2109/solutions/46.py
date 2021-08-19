n = int(input())
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if a == b:
        print(2 * a - 2)
    else:
        c = int((a * b) ** (1 / 2))
        if c * c == a * b:
            c -= 1
        if c * c + c >= a * b:
            print(2 * c - 2)
        else:
            print(2 * c - 1)
