t=int(input())
arr=input().split()
sum=[]
i=0
while(i<len(arr)):
    if(i==0):
        sum.append(int(arr[0]))
    elif(i==1):
        sum.append(int(arr[0])+int(arr[1]))
    elif(i==2):
        sum.append(max(sum[i-2]+int(arr[i]),sum[i-1],int(arr[2])+int(arr[1])))        
    else:
        sum.append(max(max(sum[i-1], sum[i-2]+ int(arr[i])), int(arr[i]) +int(arr[i-1]) + sum[i-3]))
    i=i+1
print(sum[t-1])
