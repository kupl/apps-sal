        
for _ in range(int(input())):    
    n=int(input())
    a=[int(i) for i in input().split()]
    count=0
    for i in range(n-1):
        if a[i] == a[i+1]:
            count+=1
            if count==2:
                print("Yes")
                break
        else:
            count=0
    else:
        print("No")

