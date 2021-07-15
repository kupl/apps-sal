# cook your dish here
def ch(a):
 for i in range(1,len(a)):
  if a[i]-a[i-1]>d:return False
 return True
for i in range(int(input())):
 n,d=list(map(int,input().split()))
 a=list(map(int,input().split()))
 b=a[0]
 a.sort()
 ind=a.index(b)
 i=ind
 if not ch(a):print("NO")
 else:
  arr1=[]
  arr2=[]
  arr3=[]
  arr4=[]
  i=0
  uind=ind
  if ind!=n-1:uind+=1
  while i<=uind:
   arr1.append(a[i])
   if i+1<=uind:arr2.append(a[i+1])
   i+=2
  if i:i=ind-1
  while i<n:
   arr3.append(a[i])
   if i+1<n:arr4.append(a[i+1])
   i+=2
  if (ch(arr1) and ch(arr2)) or (ch(arr3) and ch(arr4)):print("YES")
  else:print("NO")

