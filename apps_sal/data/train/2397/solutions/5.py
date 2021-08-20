def check(x, nums, k):
    small = x + 1
    for i in nums:
        if i <= x:
            small -= 1
    if small <= (k - 1) // 2:
        return False
    return True


def solve(nums, m, ans):
    n = len(nums)
    low = 0
    high = pow(2, m) - 1
    x = 0
    k = pow(2, m) - n
    while low <= high:
        mid = (low + high) // 2
        if check(mid, nums, k):
            x = mid
            high = mid - 1
        else:
            low = mid + 1
    x = bin(x)[2:]
    if len(x) < m:
        x = '0' * (m - len(x)) + x
    ans.append(x)


def main():
    t = int(input())
    ans = []
    for i in range(t):
        (n, m) = list(map(int, input().split()))
        nums = set()
        for j in range(n):
            x = int(input(), 2)
            nums.add(x)
        solve(nums, m, ans)
    for i in ans:
        print(i)


main()
