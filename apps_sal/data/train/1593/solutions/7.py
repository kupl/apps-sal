def notes(a):
    Q = [100, 50, 10, 5, 2, 1]
    (x, b) = (0, 0)
    for i in Q:
        b = a // i
        x += b
        a = a - i * b
    return x


n = int(input())
for i in range(n):
    m = int(input())
    print(notes(m))
