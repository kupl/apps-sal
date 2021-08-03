nums = [x for x in input().split()]
x = 1
for _ in range(int(nums[0])):
    b, exp = float(nums[x]), float(nums[x + 1])
    x += 2
    ans = b * (10 ** exp)
    print(f'{ans:.2f}')
