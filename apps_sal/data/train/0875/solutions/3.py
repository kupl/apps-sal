for _ in range(int(input())):
    n, z1, z2 = map(int, input().split())
    num1 = [int(i) for i in input().split()]
    num2 = [int(i) * -1 for i in num1]
    nums = num1 + num2
    f = 0
    if z1 in nums or z2 in nums:
        f = 1
        print(1)
        continue
    cnt = 0
    for val in nums:
        if val - z1 in nums or val - z2 in nums:
            cnt += 1
    if f == 0 and cnt == n + n:
        print(2)
        f = 2
    if not f:
        print(0)
