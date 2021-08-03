def longest_subsequence(_list):
    return "".join(map(str, _list))


def __starting_point():
    t = int(input())
    for _ in range(t):
        n = input()
        _list = list(map(int, input().split()))
        print(longest_subsequence(_list))


__starting_point()
