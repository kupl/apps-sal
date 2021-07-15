n=int(input())
arr=[]
val=int(input())
arr.append(val)
print(1)
for i in range (n-1) :
    val=int(input())
    count=1
    for j in arr :
        if val<j :
            count+=1
    arr.append(val)
    print(count)
