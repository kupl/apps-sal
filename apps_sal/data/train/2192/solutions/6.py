def main():
    n = int(input())
    bb = [0] * 1000001
    for _ in range(n):
        a, b = list(map(int, input().split()))
        bb[a] = b
    a = 0
    for i, b in enumerate(bb):
        if b:
            a = (bb[i - b - 1] + 1) if i > b else 1
        bb[i] = a
    print(n - max(bb))


def __starting_point():
    main()

__starting_point()
