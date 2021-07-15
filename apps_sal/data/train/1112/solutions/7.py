# cook your dish here
n=int(input())
for _ in range(n):
    m=int(input())
    count=1
    for i in range(m):
        for j in range(1,m+1-i):
            print(count,end="")
            count+=1
        print()
            
            
        
