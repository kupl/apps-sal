t = int(input())
for _ in range(t):
    n = int(input())
    ar = [int(num) for num in input().split()]
    res = 0
    for i in range(31):
        one = zero = 0
        for ele in ar:
            if ele & 1 << i:
                one += 1
            else:
                zero += 1
        if one > zero:
            res += zero * (1 << i)
        else:
            res += one * (1 << i)
    print(res)
