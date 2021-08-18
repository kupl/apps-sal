
n = int(input())
for i in range(n):
    num = int(input())

    mul = 1
    while num:
        a = (num % 10)
        num //= 10
        if a == 7 or a == 9:
            mul *= 4
        else:
            mul *= 3

    print(mul % 1000000007)
