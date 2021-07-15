t = int(input())
while(t>0):
    n = int(input())
    temp1 = ((n*n)*(n+1)*(n+1))/4
    n = n-1
    temp2 =  ((n*n)*(n+1)*(n+1))/4
    print(int(temp1+temp2))
    t-=1
