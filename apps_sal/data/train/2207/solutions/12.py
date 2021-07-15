def main():
    n = int(input())
    LIVE, DEAD = [0, 0, 0], [0, 0, 0]
    for _ in range(n):
        t, x, y = map(int, input().split())
        LIVE[t] += x
        DEAD[t] += y
    for _ in 1, 2:
        print(('LIVE', 'DEAD')[LIVE[_] < DEAD[_]])


def __starting_point():
    main()
__starting_point()
