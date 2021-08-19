# cook your dish here
n = int(input())
cost = list(map(int, input().split()))


def func(arr, n):
    a = [0] * n
    a[0] = arr[0]
    a[1] = arr[1]
    for i in range(2, n):
        a[i] = arr[i] + min(a[i - 1], a[i - 2])
    return a[-1]


ans1 = func(cost, n)
cost.reverse()
ans2 = func(cost, n)
print(min(ans1, ans2))
