[n,d]=[int(i) for i in input().split()];
x=[int(i) for i in input().split()];
s=0;
if(n>2):
    j=2;
    for i in range(0,n-2):
        while((j<n) and (x[j]-x[i]<=d)):
            j=j+1
        s=s+(j-i-1)*(j-i-2)//2;
    print(s);
else:
    print((0));

