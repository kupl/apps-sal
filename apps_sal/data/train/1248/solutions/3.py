# cook your dish here
n = int(input())


def dig(num, b):
    c = 0
    mul = b
    while(True):
        if(num // mul != 0):
            mul = mul * b
            c += 1
        else:
            break
    return c


for q in range(n):
    num = int(input())
    res = 0
    for i in range(3, num):
        po = dig(num, i)
        if((2 * (i**po) - 1) >= num):
            res += 1
    if(num == 2):
        res = res + 1
    if(num > 2):
        res = res + 2
    if(num == 1):
        print("INFINITY")
    else:
        print(res)
