t = int(input())


def length(x):
    return x**2 + x


def is_valid(count_0, count_1):
    return count_0 == count_1 ** 2


while t:
    t -= 1
    inputs = input()
    counts_1 = []
    n = len(inputs)
    cnt = 0
    for i in range(n):
        if inputs[i] == '1':
            cnt += 1
        counts_1.append(cnt)
    del i
    res = 0
    a = 1
    x = length(a)
    while x <= n:
        if is_valid(x - counts_1[x - 1], counts_1[x - 1]):
            res += 1
        i = x
        while i <= n - 1:
            cnt_1 = counts_1[i] - counts_1[i - x]
            cnt_0 = x - cnt_1
            if is_valid(cnt_0, cnt_1):
                res += 1
                i += 1
            else:
                i += abs(a - cnt_1)

        a += 1
        x = length(a)
    print(res)
