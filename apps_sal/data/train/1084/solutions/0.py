# cook your dish here
s=input()
s1=s[::-1]
arr=[]
cnt=0
for i in range(len(s1)):
 arr.append(s1[i])
for i in range(len(arr)):
 if(arr[i]=="1"):
  for j in range(i,len(arr)):
   if(arr[j]=="1"):
    arr[j]="0"
   else:
    arr[j]="1"
  cnt+=1
print(cnt)
