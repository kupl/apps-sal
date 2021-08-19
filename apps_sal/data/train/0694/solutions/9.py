def find_lcm(num1, num2):
    if num1 > num2:
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while rem != 0:
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2) / int(gcd))
    return lcm


s = int(input())
for i in range(s):
    n = int(input())
    n = n * 24
    li = list(map(int, input().split(' ')))
    num1 = li[0]
    num2 = li[1]
    lcm = find_lcm(num1, num2)
    for i in range(2, len(li)):
        lcm = find_lcm(lcm, li[i])
    print(int(n / lcm))
