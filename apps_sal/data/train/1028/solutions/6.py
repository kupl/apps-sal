# cook your dish here
t=int(input())
for i in range(1,t+1):
    num=int(input())
    n=str(num)
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** len(n)
        temp //= 10

    if num == sum:
        print("FEELS GOOD")
    else:
        print("FEELS BAD")
    

