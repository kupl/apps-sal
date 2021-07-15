t= int(input())
while(t>0):
    n = int(input())
    m=0
    m=n//(2**11)
    n%=(2**11)
    while(n>0):
        num=n%2
        m+=num
        n//=2
    print(m)
    t-=1
