t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    count=0
    i=0
    j=1
    while(i<n and j<n):
        if(a[i]==a[j]):
            count=count+1
        i=i+1
        j=j+1
    print(count)
