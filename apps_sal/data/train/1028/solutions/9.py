for _ in range(int(input())):
    num = int(input())
    s = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        s += digit ** len(str(num))
        temp //= 10

    if num == s:
        print("FEELS GOOD")
    else:
        print("FEELS BAD")
