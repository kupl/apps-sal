for _ in range(int(input())):
   n=int(input())
   dct={}
   l=list(map(int,input().split()))
   for i in range(n):
     if l[i] in dct:
       dct[l[i]].append(i)
     else:
       dct[l[i]]=[i]
   d2={}
   flag=True
   m=0
   for i in dct:
     d2[i]=len(dct[i])
     m=max(m,d2[i])
   if(m>n//2):
     print("No")
     continue
   k=list(d2.keys())
   def fun(itm):
     nonlocal d2
     return d2[itm]
   k.sort(key=fun,reverse=True)
   ans=[None]*n
   j=len(k)
   rem=[None]*j
   place=[0]*j
   for i in range(j):
     rem[i]=d2[k[i]]
   ch=1
  # print(k)
   for i in range(j):
     while(d2[k[i]]!=0):
       d2[k[i]]-=1
       if(rem[ch]==0):
         ch=(ch+1)%j
       ans[dct[k[i]][place[i]]]=k[ch]
       place[i]+=1
       rem[ch]-=1
      #     print(ans)
   print("Yes")
   for i in ans:
     print(i,end=" ")
   print("")
