from sys import stdin
t=int(stdin.readline().strip())
for i in range(t):
    a,b,n=list(map(int,stdin.readline().strip().split()))
    x=a^b
    arr=[a,b,x]
    n=n%3
    print(arr[n])
    
    

