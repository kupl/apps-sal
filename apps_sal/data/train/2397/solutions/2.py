import bisect
for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    ban = []
    for i in range(n):
        a = input()
        ban.append(int(a, 2))
    ban.sort()
    k = 2 ** m - n
    start = 0
    end = 2 ** m

    def func(num):
        res = num
        index = bisect.bisect_left(ban, num)
        res -= index
        return res
    while end - start > 1:
        test = (end + start) // 2
        if (k - 1) // 2 >= func(test):
            start = test
        else:
            end = test
    if (k - 1) // 2 >= func(end):
        ans = end
    else:
        ans = start
    ban = set(ban)
    while ans in ban:
        ans -= 1
    res = bin(ans)[2:]
    res = '0' * (m - len(res)) + res
    print(res)
