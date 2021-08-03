# cook your dish here
def check(mid):
    time = 0.0
    for i in range(n):
        if time <= arr[i]:
            time = arr[i] + mid
        elif time <= arr[i] + d:
            time += mid
        else:
            return False
    return True


for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr.sort()
    low = 0
    high = 10000000000
    while ((high - low) > 0.000001):
        mid = low + (high - low) / 2
        if check(mid):
            ans = mid
            low = mid
        else:
            high = mid
    print("{0:.6f}".format(ans))
