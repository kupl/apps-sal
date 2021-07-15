
def hantei(x,y):

    if y == 0:
        return "l"
    elif x == R:
        return "d"
    elif y == C:
        return "r"
    elif x == 0:
        return "u"

    return "n"

R,C,N = list(map(int,input().split()))

u = []
l = []
d = []
r = []

for i in range(N):

    X1,Y1,X2,Y2 = list(map(int,input().split()))

    if hantei(X1,Y1) != "n" and hantei(X2,Y2) != "n":


        if hantei(X1,Y1) == "l":
            l.append([X1,Y1,i])
        elif hantei(X1,Y1) == "d":
            d.append([X1,Y1,i])
        elif hantei(X1,Y1) == "r":
            r.append([X1,Y1,i])
        elif hantei(X1,Y1) == "u":
            u.append([X1,Y1,i])

        X1 = X2
        Y1 = Y2
    
        if hantei(X1,Y1) == "l":
            l.append([X1,Y1,i])
        elif hantei(X1,Y1) == "d":
            d.append([X1,Y1,i])
        elif hantei(X1,Y1) == "r":
            r.append([X1,Y1,i])
        elif hantei(X1,Y1) == "u":
            u.append([X1,Y1,i])

l.sort()
d.sort()
r.sort()
r.reverse()
u.sort()
u.reverse()

ps = []
for i in l:
    ps.append(i[2])
for i in d:
    ps.append(i[2])
for i in r:
    ps.append(i[2])
for i in u:
    ps.append(i[2])

q = []

for i in ps:
    if len(q) > 0 and q[-1] == i:
        del q[-1]
    else:
        q.append(i)

if len(q) == 0:
    print ("YES")
else:
    print ("NO")


