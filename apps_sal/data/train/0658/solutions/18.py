for i in range(int(input())):
    n = int(input())
    dp = [[1 for k in range(n)] for k in range(2)]  # row 1: longest UD, row 2: longest DU
    nums = [int(i) for i in input().split()]
    answer = 0
    for k in range(n - 2, -1, -1):
        if nums[k + 1] >= nums[k]:
            dp[0][k] = 1 + dp[1][k + 1]
            if dp[0][k] > answer:
                answer = dp[0][k]
        if nums[k + 1] <= nums[k]:
            dp[1][k] = 1 + dp[0][k + 1]

    answer += 1
    for k in range(n - 1):
        if k + dp[0][k] >= n:
            continue
        possible = 0
        if dp[0][k] % 2 == 0:
            possible = dp[0][k] + dp[1][k + dp[0][k]] + 1
        else:
            possible = dp[0][k] + dp[0][k + dp[0][k]] + 1
        if possible > answer:
            answer = possible

    print(answer)
