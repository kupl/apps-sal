# cook your dish here
for _ in range(int(input())):
    s = input().split()
    n = int(s[0])
    s1 = s[1]
    a, b = 0, 0
    for i in range(n):
        x = input()
        if(x[0] == '0'):
            k0 = x.count('0')
            a += k0
        else:
            k1 = x.count('1')
            b += k1
    if(a == b):
        if(s1 == "Dee"):
            print("Dum")
        else:
            print("Dee")
    else:
        if(a > b):
            print("Dee")
        else:
            print("Dum")
