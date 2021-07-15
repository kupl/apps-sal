# cook your dish here
t = int(input())
while t>0:
    n = int(input())
    nth = (n*(n+1)*(2*n+1))//6 - n*n
    print(nth)
    t-=1
