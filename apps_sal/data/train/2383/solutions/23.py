def solve(a, b):
    min_size = min(a, b)
    max_size = max(a, b)
    if min_size * 2 <= max_size:
        return max_size * max_size
    else:
        return min_size * min_size * 4


def main():
    T = int(input())
    for _ in range(T):
        a, b = list(map(int, input().split()))
        print(solve(a, b))


def __starting_point():
    main()

__starting_point()
