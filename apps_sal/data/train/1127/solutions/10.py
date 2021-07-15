# cook your dish here
t=int(input())
def do():
    s=input()
    c=0
    v=' '
    c=s.count(v)
    if c==0:
        s=s.capitalize()
        print(s)
    elif(c==1):
        f=s.split()[0]
        l=s.split()[1]
        l=l.capitalize()
        print(f[0].capitalize(),'. ',l,sep='')
    elif(c==2):
        f=s.split()[0]
        m=s.split()[1]
        l=s.split()[2]
        l=l.capitalize()
        print(f[0].capitalize(),'. ',m[0].capitalize(),'. ',l,sep='')
    else:
        pass
    return
for i in range(t):
    do()
        

