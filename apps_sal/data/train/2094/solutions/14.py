n=int(input())
s=str(input())
count1=s.count('n')
count2=s.count('r')
arr=[1]*count1
arr1=[0]*count2
arr=arr+arr1
print(*arr)

