from math import log, pow
n = int(input())
a = []
for i in range(n):
    no = int(input())
    if(no % 2 == 0):
        a.append("0")
    elif(no == 1):
        a.append("1")
    elif(no == 3):
        a.append("3")
    else:
        s = "2"
        lv = int(log(no, 2))
        clv = 1
        cno = 3
        while(cno != no):
            if(no < cno * pow(2, lv - clv)):
                s = s + "1"
                clv = clv + 1
                cno = (2 * cno) - 1
            else:
                s = s + "2"
                clv = clv + 1
                cno = (2 * cno) + 1
        a.append(s)
for i in a:
    print(i)
