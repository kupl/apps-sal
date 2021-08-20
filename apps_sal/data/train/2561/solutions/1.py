from collections import Counter


def __starting_point():
    X = int(input().strip())
    shoes = list(map(int, input().strip().split()))
    N = int(input().strip())
    result = 0
    warhs = Counter(shoes)
    for _ in range(N):
        (size, money) = map(int, input().strip().split(' '))
        if warhs[size] > 0:
            result += money
            warhs[size] -= 1
    print(result)


__starting_point()
