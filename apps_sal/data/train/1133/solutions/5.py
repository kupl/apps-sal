def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


t = int(input())
for i in range(t):
    n = int(input())
    if(n == 1):
        cost = 1
        gcd = int(input())
    else:
        number = list(map(int, input().split()))
        num1 = number[0]
        num2 = number[1]
        gcd = find_gcd(num1, num2)
        for i in range(2, len(number)):
            gcd = find_gcd(gcd, number[i])
        cost = sum(number) // gcd
    print(str(gcd) + " " + str(cost))
