def asc_merge_sort(time,name):
 length=len(time)
 if length>1:
  # finding the middle point if the timeay
  if length%2==0:
   mid=length//2
  else:
   mid=length//2+1

  # for dividing the timeay into two sub parts
  l = time[:mid]
  r =time[mid:]
  ll = name[:mid]
  rr =name[mid:]

  # sorting the both sub timeays
  asc_merge_sort(l,ll)
  asc_merge_sort(r,rr)
  
  i=j=k=0
  while i<len(l) and j< len(r):
   if l[i]<r[j]:
    time[k]=l[i]
    name[k]=ll[i]
    i+=1
   else:
    time[k]=r[j]
    name[k]=rr[j]
    j+=1
   k+=1
  while i<len(l):
   time[k]=l[i]
   name[k]=ll[i]
   i+=1
   k+=1
  while j<len(r):
   time[k]=r[j]
   name[k]=rr[j]
   j+=1
   k+=1
 return name
for _ in range(int(input())):
 nm=[]
 tm=[]
 n=int(input())
 for i in range(n):
  nm.append(input())
  tm.append(int(input()))
 ot=asc_merge_sort(tm,nm)
 for k in ot:
  print(k)
  

