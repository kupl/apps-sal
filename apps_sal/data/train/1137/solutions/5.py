def getPairsCount(arr, n, sum):
    m = [0] * 10000001
    for i in range(0, n):
        m[arr[i]] += 1
    twice_count = 0
    for i in range(0, n):
        twice_count += m[sum - arr[i]]
        if sum - arr[i] == arr[i]:
            twice_count -= 1
    return int(twice_count / 2)


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    su = 2000
    val = getPairsCount(l, n, su)
    if val:
        print('Accepted')
    else:
        print('Rejected')
