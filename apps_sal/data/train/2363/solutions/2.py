def read_int():
    return int(input())


def read_ints():
    return list(map(int, input().split(' ')))


t = read_int()
for case_num in range(t):
    n = read_int()
    a = list(read_ints())
    a.sort()
    ans = int(1000000000.0)
    for i in range(n - 1):
        ans = min(ans, abs(a[i] - a[i + 1]))
    print(ans)
