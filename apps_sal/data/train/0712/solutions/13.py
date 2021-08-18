
def find_lcm(num1, num2):
    if (num1 > num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while (rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = (int(num1 * num2) // int(gcd))
    return lcm


t = int(input())
for num in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    if len(l) == 1:
        if l[0] % 2 == 0:
            print("NO")
        else:
            print("YES")

    else:
        num1 = l[0]
        num2 = l[1]
        lcm = find_lcm(num1, num2)

        for i in range(2, len(l)):
            lcm = find_lcm(lcm, l[i])

        if lcm % 2 == 0:
            print("NO")
        else:
            print("YES")
