for t in range(int(input())):
    (s, n) = map(int, input().split())
    x = 0
    if s % 2 != 0:
        s -= 1
        x += 1
    x += s // n
    if s % n != 0:
        x += 1
    print(x)
