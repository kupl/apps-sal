"""
observations:
1. multi solution

"""


def inc_by_mod(arr, m):
    def is_opt(count):
        prev = 0
        for elem in arr:
            if prev < elem:
                if m - (elem - prev) > count:
                    prev = elem
            elif prev - elem > count:
                return False
        return True
    count = 0
    lo, hi = 0, m - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if is_opt(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    res = inc_by_mod(arr, m)
    print(res)


def __starting_point():
    main()


__starting_point()
