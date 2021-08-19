# import sys

# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

t = int(input())

for _ in range(t):
    n = int(input())
    ar = [int(num) for num in input().split()]

    res = 0
    for i in range(31):
        one = zero = 0
        x = 1

        for j in range(n):
            if ar[j] & (x << i):
                one += 1
            else:
                zero += 1

        if one > zero:
            res += zero * (x << i)
        else:
            res += one * (x << i)

    print(res)
