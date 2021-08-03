try:
    n = int(input())
    nums = []
    for _ in range(n):
        t = int(input())
        nums.append(t)
        z = sorted(nums, reverse=True)
        rank = z.index(t)
        print(rank + 1)

except:
    pass
