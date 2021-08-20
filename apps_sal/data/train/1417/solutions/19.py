t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    nums = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in a:
        nums[i - 1] += 1
    if min(nums) == 0:
        print(0)
    else:
        print(min(nums))
