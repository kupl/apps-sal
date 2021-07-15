#Note that it's python3 Code. Here, we are using input() instead of raw_input().
#You can check on your local machine the version of python by typing "python --version" in the terminal.

n,k=list(map(int, input().split()))
i=1
sum=0
while i<=n:
    
    z=int(input())
    if z%k==0:
        sum=sum+1
        i=i+1
    else:
        i=i+1 
    
print(sum)

