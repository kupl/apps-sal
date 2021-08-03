# cook your dish here
for i in range(int(input())):
    a = input()
    a = int(a, 2)
    b = input()
    b = int(b, 2)
    num = 0
    while(b > 0):
        u = a ^ b
        v = a & b
        a = u
        b = v * 2
        num += 1
    print(num)
