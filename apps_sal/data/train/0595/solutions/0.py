def binarySearch(arr, l, r, x):
 mid=0
 while l <= r: 
  mid = l + (r - l)//2; 
  if arr[mid] == x: 
   return mid+1 
  elif arr[mid] < x: 
   l = mid + 1
  else: 
   r = mid - 1
 if mid!=len(arr):
  if arr[mid]<x:
   return mid+1
 return mid
s=input()
strt=[]
end=[]
plc=[]
landr=[]
l2r=[]
lr=[]
ans=0
n=len(s)
if n!=1:
 for i in range(n):
  strt.append([])
  end.append([])
  landr.append([0]*n)
  l2r.append([0]*n)
 for i in range(n):        
  for j in range(n):
   if i-j<0 or i+j>=n:
    break
   if (s[i-j]==s[i+j]):
    if i-j-1>=0:
     strt[i-j-1].append(2*j+1)
    if i+j+1<n:
     end[i+j+1].append(2*j+1)
   else:
    break
 for i in range(n):
  for j in range(n):
   if i-j<0 or i+j+1>=n:
    break
   if (s[i-j]==s[i+j+1]):
    if i-j-1>=0:
     strt[i-j-1].append(2*j+2)
    if i+j+2<n:
     end[i+j+2].append(2*j+2)
   else:
    break
 for i in range(n):
  end[i].sort()
  strt[i].sort()
 for i in range(n-1):
  for j in range(i+1,n):
   if s[i]==s[j]:
    lr.append([i,j])
    if i>0 and j<n-1:
     landr[i][j]=landr[i-1][j+1]+1
    else:
     landr[i][j]=1
 for i in lr:
  tempans=1
  l=i[0]
  r=i[1]
  length=r-l-1
  tempans+=binarySearch(strt[l],0,len(strt[l])-1,length)
  tempans+=binarySearch(end[r],0,len(end[r])-1,length)
  l2r[l][r]=tempans
 for i in range(n):
  for j in range(n):
   ans+=l2r[i][j]*landr[i][j]
print(ans)
