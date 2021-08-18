
T = eval(input())


def is_equal(ar, D):
    N = len(ar)
    last = -1
    for i in range(D):
        count = 0
        ans = 0
        for j in range(i, N, D):
            ans += ar[j]
            count += 1
        if ans % count != 0:
            return -1
        if last == -1:
            last = ans / count
        else:
            if last != ans / count:
                return -1
    return last


def solve(ar, D, equal):
    ans = 0
    N = len(ar)
    for i in range(D):
        for j in range(i, N - D, D):
            diff = ar[j] - equal
            ar[j] -= diff
            ar[j + D] += diff
            ans += abs(diff)
    return ans


for _ in range(T):
    N, D = list(map(int, input().split(" ")))
    ar = list(map(int, input().split(" ")))
    ans = is_equal(ar, D)
    if ans == -1:
        print(-1)
    else:
        print(solve(ar, D, ans))
