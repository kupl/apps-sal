def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in [0] * n]
    if all([a == b for a, b in ab]):
        print(0)
        return 0
    min_b = min([b for a, b in ab if a > b])
    sum_a = sum([a for a, b in ab])
    print(sum_a - min_b)


main()
