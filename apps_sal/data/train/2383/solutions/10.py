def read_int():
    return int(input())


def read_ints():
    return list(map(int, input().split(' ')))


t = read_int()
for case_num in range(t):
    a, b = read_ints()
    x = max(2 * min(a, b), max(a, b))
    print(x * x)
