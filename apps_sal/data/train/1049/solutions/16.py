# cook your dish here
for _ in range(int(input())):
    n, k = input().split()
    n, k = int(n), int(k)
    nums = list(map(int, input().split()))

    length1 = len(set(nums))
    i = 0
    j = k - 1
    initial = sum(nums[i:j + 1])
    if len(set(nums)) == length1:
        m = initial
    else:
        m = 0
    while j < len(nums):
        # print(i,j,initial)
        j += 1
        if j == len(nums):
            break
        initial -= nums[i]
        i += 1
        initial += nums[j]
        if len(set(nums[i:j + 1])) == length1:
            m = max(m, initial)

    print(m)
