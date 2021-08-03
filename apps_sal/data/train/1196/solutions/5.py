def maxSum(arr, n, k):
    res = 0
    for i in range(k):
        res += arr[i]
    curr_sum = res
    for i in range(k, n):
        curr_sum += arr[i] - arr[i - k]
        res = max(res, curr_sum)
    return res


for _ in range(int(input())):
    n, m, k = map(int, input().split())
    ma = 0
    J = []
    for i in range(n):
        a = [int(x) for x in input().split()]
        s1 = maxSum(a, m, k)
        if ma < s1:
            ma = s1
        J.append(a)
        # print(J)
    for i in range(m):
        arr = [x[i] for x in J]
        ss = maxSum(arr, n, k)
        if ma < ss:
            ma = ss
    print(ma)
