for t in range(int(input())):
    (R, C) = list(map(int, input().split()))
    (x, y) = list(map(int, input().split()))
    l = [x + y, R - 1 - x + y, C - y - 1 + x, R - x + C - y - 2]
    print(max(l))
