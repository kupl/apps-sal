def getSum(s1):
    sum = 0
    for c in s1:
        if c.isdigit():
            sum += int(c)
    return sum


T = int(input())
for i in range(T):
    s = input()
    print(getSum(s))
