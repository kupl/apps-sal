# cook your dish here
def ub(arr, item):
    n = len(arr)
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return low


def lb(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return high


def main():
    n, x, y = map(int, input().split())
    timing = []
    for i in range(n):
        p, q = map(int, input().split())
        timing.append((p, q))

    v = list(map(int, input().split()))

    w = list(map(int, input().split()))
    timing.sort()
    v.sort()
    w.sort()

    mn = 1e18

    for i in range(n):
        s = lb(v, timing[i][0])
        e = ub(w, timing[i][1])
        if s >= 0 and e < y:
            mn = min(mn, abs(v[s] - w[e]) + 1)

    print(mn)


main()
