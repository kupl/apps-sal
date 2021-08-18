def sticks(nums):
    ans = []
    it = 0

    while it < len(nums) - 2:

        if nums[it] + nums[it + 1] > nums[it + 2]:

            ans = []
            for p in range(2, -1, -1):
                ans.append(nums[it + p])

        it += 1

    if not nums:
        return False

    return ans


num = int(input())
nums = list(map(int, input().split()))

temp = sticks(sorted(nums))

if temp:
    print('YES')
    print(' '.join(list(map(str, temp))))
else:
    print('NO')
