for _ in range(int(input())):
    num = int(input())
    order = len(str(num))
    suma = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        suma += digit ** order
        temp //= 10
    if num == suma:
        print("FEELS GOOD")
    else:
        print("FEELS BAD")

