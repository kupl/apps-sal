n=int(input())
arr=[]
val=int(input())
arr.append(val)
print(1)
for i in range (n-1) :
    val=int(input())
    arr.append(val)
    arr.sort(reverse=True)
    count=arr.index(val)
    print(count+1)
