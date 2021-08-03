t = int(input())
for i in range(0, t):

    num = int(input())

    order = len(str(num))

    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print("FEELS GOOD")
    else:
        print("FEELS BAD")
