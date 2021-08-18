def find_lcm(num1, num2):
    if(num1 > num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2) / int(gcd))
    return lcm


for _ in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    num1 = x[0]
    num2 = x[1]
    lcm = find_lcm(num1, num2)
    lcm = find_lcm(lcm, x[2])
    n = n * 24
    print(int(n / lcm))
