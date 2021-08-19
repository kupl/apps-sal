# cook your dish here
n = int(input())
l1 = []
for i in range(0, n):
    l1.append(int(input()))
for item in l1:
    num1 = 0
    a = item % 100
    if(a == 0):
        num1 += (item / 100)
    else:
        num1 += ((item - a) / 100)
        b = a % 50
        if(b == 0):
            num1 += (a / 50)
        else:
            num1 += ((a - b) / 50)
            c = b % 10
            if(c == 0):
                num1 += (b / 10)
            else:
                num1 += ((b - c) / 10)
                d = c % 5
                if(d == 0):
                    num1 += (c / 5)
                else:
                    num1 += ((c - d) / 5)
                    e = d % 2
                    if(e == 0):
                        num1 += (d / 2)
                    else:
                        num1 += ((d - e) / 2)
                        f = e % 1
                        if(f == 0):
                            num1 += (e)
    print(int(num1))
