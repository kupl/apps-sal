import sys
input=sys.stdin.readline
n,m=map(int,input().split())
for i in range(n//2+n%2):
    x1=i+1
    x2=n-i
    if(x1==x2):
        for j in range(m//2+m%2):
            if(j+1==m-j):
                sys.stdout.write((str(x1)+" "+str(j+1)+"\n"))
            else:
                sys.stdout.write((str(x1)+" "+str(j+1)+"\n"))
                sys.stdout.write((str(x2)+" "+str(m-j)+"\n"))
    else:
        if(i%2==0):
            for j in range(m):
                sys.stdout.write((str(x1)+" "+str(j+1)+"\n"))
                sys.stdout.write((str(x2)+" "+str(m-j)+"\n"))
        else:
            for j in range(m):
                sys.stdout.write((str(x1)+" "+str(m-j)+"\n"))
                sys.stdout.write((str(x2)+" "+str(j+1)+"\n"))
