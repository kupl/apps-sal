# cook your dish here
n = int(input())
nums = list(map(int, input().split()))
if n < 3:
    print(0)
else:
    for i in range(3, n):
        nums[i] = nums[i] + min(nums[i-1], nums[i-2], nums[i-3])
    print(min(nums[-1], nums[-2], nums[-3]))

