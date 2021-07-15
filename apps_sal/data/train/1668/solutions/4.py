#先确定要改变的范围，然后在对指定范围进行改动
#itertools是很好用的包，注意学习
import itertools
def next_smaller(n):
    print(n)
    a=list(str(n))
    b=len(a)
    if b==1:
        return -1
    for j in range(b-2,-1,-1):
        if a[j] > a[j+1]:         
            t=a[j:]
            m=max([x for x in t if x<t[0]])
            t.remove(m)
            c=[]
            while len(t)>0:
                d=max(t)
                c.append(d)
                t.remove(d)
            a[j:]=[m]+c
            if a[0]=='0':
                return -1
            return int(''.join(a))
    return -1

