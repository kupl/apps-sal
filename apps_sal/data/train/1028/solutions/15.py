for i in range(int(input())):
    n = int(input())
    sum = 0
    t = n
    while t > 0:
        digit = t % 10
        sum += digit ** len(str(n))
        t //= 10
    if(n==sum):
        print("FEELS GOOD")
    else:
        print("FEELS BAD")
