# cook your dish here
t=int(input())
v=[1,5,9,15,21]
s={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
for i in range(t):
    x=input()
    l=list(x)
    d=[]
    for j in range(len(x)):
        a=s.get(l[j])
        m=[]
        for k in range(5):
            x=abs(a-v[k])
            m.append(x)
        d.append(min(m))
    print(sum(d))

