from math import acos,sqrt,pi

def norm(x):
    if x==0:
        return 0
    else:
        return sqrt(scalar(x,x))

def scalar(x,y):
    return sum([x[i]*y[i] for i in range(5)])
def vector(p,q):
    return ([ (q[i]-p[i]) for i in range(5) ])

number=0
good_points=[]

n=int(input())
liste=[]
for _ in range(n):
    x=list(map(int,input().split(" ")))
    liste.append(x)

if n>11:
    print(0)
else:
    for i in range(n):
        bool=True
        for j in range(n):
            if j!=i:
                for k in range(n):
                    if k!=j and k!=i:
                        x=vector(liste[i],liste[j])
                        y=vector(liste[i],liste[k])
                        angle=acos(scalar(x,y)/norm(x)/norm(y))
                        if angle<pi/2:
                            bool=False
        if bool:
            good_points.append(i+1)
            number+=1
    if number>0:
        answer=str(number)+' '
        good_points.sort()
        for element in good_points:
            answer+='\n'+str(element)
        print(answer)
    else:
        print(0)
