t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    s = sum(nums)
    if s == 0:
        print(1)
    else:
        l = 9999999
        sum1 = 0
        step = False
        ini = 0
        f = 0
        for i in range(n):
            sum1 += nums[i]
            while sum1 >= s and ini <= i:
                l = min(l, i - ini + 1)
                if l == 1:
                    f = 1
                    break
                sum1 -= nums[ini]
                ini += 1
                step = True
            if f == 1:
                break
            if step:
                sum1 -= nums[ini]
                ini += 1
        if f == 1:
            print(1)
        elif l != 9999999:
            print(l)
        else:
            print(1)
