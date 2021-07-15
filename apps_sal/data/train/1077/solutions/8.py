n=int(input())
while n>0:
    t=int(input())
    i=t
    a=[]
    while t>0:
        r=input().split()
        a.append(r)
        t-=1
    p=''
    while i>0:
        r=a[i-1]
        j=r[0]
        if t==0:
            r[0]='Begin'
            t=1        
        elif p=='Right':
            r[0]='Left'
        elif p=='Left':
            r[0]='Right'
        r=' '.join(r)
        print(r)
        i-=1
        p=j
    print('\n')
    n-=1

