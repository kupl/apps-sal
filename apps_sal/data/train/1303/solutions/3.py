# cook your dish here
M = 10**9+7
for _ in range(int(input())):
    n,k,m=(int(s) for s in input().split())
    l = [int(s)%m for s in input().split()]
    ans = [0]*(k+1)
    i = 1
    for j in range(n):
     mov = 0
     just = 0
     if (i%m+1)%m==l[j] and i<k:
      if ans[i]!=0:
       just=1
      mov = 1
     w = i - (i%m-l[j])%m
     while w>=1:
      if w==1:
       ans[w]+=1
      else:
       ans[w]+=ans[w-1]
      w-=m
     if mov:
      i+=1
      if just:
       ans[i] = ans[i-1]
    print(ans[k]%M) 
