# cook your dish here
for _ in range(int(input())):
    n=int(input())
    arr=[int(i) for i in input().split()]
    arr=sorted(arr)
    for i in range(n):
       
        if i%2==0:
            if i==n-1:
                print(arr[i],'',end='')
            else:
                print(arr[i+1],'',end='')
        else:
            print(arr[i-1],'',end='')
    print()
            
            
    
