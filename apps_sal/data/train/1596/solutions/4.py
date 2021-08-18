import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    X, Y = list(map(int, input().split()))
    x = X + 1
    y = Y + 1

    def bit(x):
        a = []
        while x > 0:
            a.append(x & 1)
            x = x // 2

        return sum(a)

    count_x = bit(x)
    count_y = bit(y)

    if count_x < count_y:
        print('1', count_y - count_x)
    elif count_y < count_x:
        print('2', count_x - count_y)
    else:
        print('0', '0')
