# cook your dish here
def solve():
    n=int(input())
    i=0
    while i<n:
        j=n-i
        for l in range(i):
            print("*",end="")
        while(j>=1):
            print(j,end="")
            j-=1
        print()    
        
        i+=1    

t=int(input())
i=0
while(i<t):
    solve()
    i+=1
