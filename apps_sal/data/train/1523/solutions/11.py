
# def recursive(List, taken_previous, idx, r) :
#     if idx >= N : return 0
#     if taken_previous :
#         # I am not sure if you should go 2 steps even futher to check. Probably extra recursion
#         return List[idx] + max( recursive(List, False, idx + 2, r + List[idx]), recursive(List, False, idx + 3, r + List[idx]))
#     else :
#         return  List[idx] + max( recursive(List, True, idx + 1, r + List[idx]), recursive(List, False, idx + 2, r + List[idx]) )

# N = int(input())
# fees = list(map(int, input().split()))
# dp = [-1] * int(1e6)

# def recursive(nums, n) :
#     if n < 0  : return 0
#     elif n == 0 : return nums[0]
#     elif n == 1 : return nums[0] + nums[1]
#     else :
#         if dp[n] != -1 : return dp[n]

#         dp[n] = max( recursive(nums, n - 1),
#                      recursive(nums, n - 2) + nums[n],
#                      recursive(nums, n - 3) + nums[n] + nums[n-1]
#                     )

#         return dp[n]


# if N <= 2 :  print(sum(fees))
# else :
#     r = recursive(fees, N - 1)
#     print(r)


dp = [-1] * int(1e6)


def solve(a, d):
    if d < 0:
        return 0
    if d == 0:
        return a[0]
    if d == 1:
        return a[0] + a[1]

    if dp[d] != -1:
        return dp[d]

    dp[d] = max(
        solve(a, d - 1),
        solve(a, d - 2) + a[d],
        solve(a, d - 3) + a[d] + a[d - 1]
    )
    return dp[d]


def main():
    from sys import stdin, stdout, setrecursionlimit
    setrecursionlimit(int(1e6))
    rl = stdin.readline

    n = int(rl())
    a = [int(x) for x in rl().split()]

    if n < 3:
        stdout.write(str(sum(a)))
        return

    stdout.write(str(solve(a, n - 1)))


main()
