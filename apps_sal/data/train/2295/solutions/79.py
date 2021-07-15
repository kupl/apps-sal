import sys
input = sys.stdin.readline

n = int(input())
a = []
b = []


res = 0

for i in range(n):
    aa,bb = map(int,input().split())
    a.append(aa)
    b.append(bb)

def f(a,b):
    c = []
    d = []
    judge = True

    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            judge = False
    if judge:
        return cnt,c,d
    
    for i in range(len(a)):
        if a[i] <= b[i]:
            cnt += b[i]
        else:
            c.append(a[i])
            d.append(b[i])
    if len(c) == 1 or max(d) == 0:
        return cnt,[],[]
    else:
        mi = min(d)
        flag = True
        pl_flag = True
        for i in range(len(c)):
            if d[i] == mi and flag:
                c[i] = d[i] + 1
                flag = False
            else:
                if pl_flag and d[i] > 0:
                    c[i] = d[i]-1
                    pl_flag = False
                else:
                    c[i] = d[i]
        return cnt,c,d

while True:
    plus,a,b = f(a,b)
    res += plus
    if a == []:
        print(res)
        break
