t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    k = int(input())
    an = nums[k - 1]
    cn = 0
    for i in range(n):
        if nums[i] < an:
            cn += 1
    print(cn + 1)
