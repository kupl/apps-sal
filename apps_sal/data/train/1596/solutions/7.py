t = int(input())
for _ in range(t):
    (x, y) = list(map(int, input().split()))
    if x == y:
        print(0, 0)
    else:
        x_count = bin(x + 1).count('1')
        y_count = bin(y + 1).count('1')
        if x_count == y_count:
            print(0, 0)
        elif x_count < y_count:
            print(1, y_count - x_count)
        else:
            print(2, x_count - y_count)
