f=input()
f=[int(x) for x in f]
def func():
    if f.count(1)==len(f):
        for i in f[:-1]:print(i,end='')
        return
    elif f.count(0)==len(f):
        print(0)
        return
    start=False
    j=-1
    for i in f:
        j+=1
        if start==False and i==0:
            continue
        start=True
        if i==0:
            j+=1
            break
        print(i,end='')
    while j<len(f):
        print(f[j],end='')
        j+=1

func()

