# bit_cracker007 #
test = eval(input())
a = []
b = []
top = -1
for i in range(test):
    x = input().split()
    if(x[0] != "-1" and x[0] != "0"):
        n = int(x[0])
        if top > -1 and n > a[top][0]:
            b[top] += 1
        else:
            a.append((n, x[1]))
            b.append(0)
            top += 1
    elif (x[0] == "-1"):
        print("%s %s" % (b[top], a[top][1]))
        a.pop()
        b.pop()
        top -= 1
