# cook your dish here
n=int(input())
array=list(map(int, input().split()))
appo2=sum(array)
for i in range(3,n):
    array[i]+=min([array[i-1],array[i-2],array[i-3]])
appo=min([array[-1],array[-2],array[-3]])
print(appo2-appo)

