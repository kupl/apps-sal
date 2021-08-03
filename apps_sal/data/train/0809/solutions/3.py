# cook your dish here
n = int(input())
nums = list(map(int, input().strip().split(" ")))
if n < 3:
    print("NO")
else:
    nums.sort(reverse=True)
    l = nums[0]
    m = nums[1]
    s = nums[2]
    trig = 1
    for i in range(0, n - 2):
        s = nums[i + 2]
        if l < m + s:
            trig = 0
            print("YES")
            print(l, m, s)
            break
        l = m
        m = s
    if trig:
        print("NO")
