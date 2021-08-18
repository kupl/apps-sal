def function(n, arr, i, dp):
    if i >= n - 1:
        sum = 0
        pointer = 1
        s = ''
        for k in arr:
            sum += (k * pointer)
            pointer += 1
            s += str(k)
        dp[s] = sum
        return sum
    s = ''
    for l in arr:
        s += str(l)
    if dp.get(s, -1) == -1:
        val = function(n, arr, i + 1, dp)
    else:
        val = dp[s]
    for j in range(i, n - 1):
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
        s = ''
        for l in arr:
            s += str(l)
        if dp.get(s, -1) == -1:
            val1 = function(n, arr, j + 2, dp)
        else:
            val1 = dp[s]
        val = val if val > val1 else val1
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return val


times = int(input())
while times > 0:
    times -= 1
    n = int(input())
    arr = [int(i) for i in input().split()]
    dp = {}
    print(function(n, arr, 0, dp))
