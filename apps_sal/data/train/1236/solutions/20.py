# cook your dish here

for _ in range(int(input())):
    n = int(input())
    arr = list(i for i in input())
    # print(arr)
    
    count=0
    char=arr[0]
    for j in range(1,n):
        if(char==arr[j]):
            # del arr[i]
            count+=1
        char = arr[j]
            
            
    
    # print(arr)
    print(count)

