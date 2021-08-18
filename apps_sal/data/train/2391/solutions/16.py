import collections

line = input()
t = int(line)
for _i in range(t):

    line = input()
    n = int(line)
    line = input()
    nums = [int(i) for i in line.split(' ')]

    res = collections.deque()
    for i in range(n - 2):
        for j in range(n - 3, i - 1, -1):
            if nums[j + 2] < nums[j + 1] and nums[j + 2] < nums[j]:
                a, b, c = nums[j + 2], nums[j + 1], nums[j]
                nums[j], nums[j + 1], nums[j + 2] = a, c, b
                res.append(j + 1)
        if nums[i] > nums[i + 1]:
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            nums[i], nums[i + 1], nums[i + 2] = b, c, a
            res.append(i + 1)
            res.append(i + 1)

    if nums[n - 3] == nums[n - 1] and nums[n - 2] > nums[n - 1]:
        res.append(n - 2)
        nums[n - 1], nums[n - 2] = nums[n - 2], nums[n - 1]
    if nums[-1] < nums[-2]:
        i = n - 2
        while i >= 0 and nums[i] != nums[i + 1]:
            i -= 1
        if i < 0:
            print(-1)
        else:
            while i < n - 2:
                res.append(i + 1)
                res.append(i + 1)
                i += 1
            print(len(res))
            for i in res:
                print(i, end=' ')
            print()
    else:
        print(len(res))
        for i in res:
            print(i, end=' ')
        print()
