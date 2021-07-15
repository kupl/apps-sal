# cook your dish here
from collections import defaultdict
for _ in range(int(input())):
   maxi=-1
   d=defaultdict(list)
   n=int(input())
   a=list(map(int,input().split()))
   even=[0]*n
   odd=[0]*n
   pref=[0]*n
   pref[0]=a[0]
   if a[0]%2==0:
       even[0]=1
   if a[0]%2==1:
       odd[0]=1
   d[a[0]].append(0)

   for i in range(1,n):
       d[a[i]].append(i)
       if a[i]%2==0:
           even[i]=even[i-1]+1
           odd[i]=odd[i-1]
       if a[i]%2==1:
           odd[i]=odd[i-1]+1
           even[i]=even[i-1]

       pref[i]=pref[i-1]+a[i]
  ## print(even)
   ##print(odd)
   for i in range(n):

       x=a[i]
       if len(d[a[i]])>=2:
           if x%2==0:
               y=d[a[i]][0]
               z=d[a[i]][1]
               ##print(even[z])
               if y==0:

                   ##print(even[z],i)
                   if even[z]%2==0:
                       maxi = max(maxi, pref[z] - pref[y] - x)
                   continue

               if (even[z]-even[y-1])%2==0:
                       maxi=max(maxi,pref[z]-pref[y]-x)
               ##print(maxi,i,"hi")

           if x%2==1:
               y = d[a[i]][0]
               z = d[a[i]][1]
               if y==0:
                  ## print(odd[z])
                   if odd[z]%2==1:
                       maxi = max(maxi, pref[z] - pref[y] - x)
                   continue

               if (odd[z] - odd[y - 1]) % 2 == 1:
                   maxi = max(maxi, pref[z] - pref[y] - x)
       d[a[i]].pop(0)
   if maxi==-1:
       print(0)
       continue
   print(maxi)





