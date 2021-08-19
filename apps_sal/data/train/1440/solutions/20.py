for _ in range(int(input())):
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    res = nums[0] % nums[1]
    for n in nums[2:]:
        res = res % n
    print(res)
