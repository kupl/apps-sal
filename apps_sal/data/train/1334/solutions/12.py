dp = [-1] * int(1e6)


def solve(nums, n):

    if n < 2:
        return 0

    if dp[n] != - 1:
        return dp[n]

    dp[n] = min(nums[n] + solve(nums, n - 1),
                nums[n - 1] + solve(nums, n - 2),
                nums[n - 2] + solve(nums, n - 3)
                )

    return dp[n]


def main():
    from sys import stdin, stdout, setrecursionlimit
    setrecursionlimit(int(5e5))
    N = int(input())
    hours = list(map(int, input().split()))
    solution = solve(hours, N - 1)
    print(solution)


main()
