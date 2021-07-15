MOD = 10**9+7
lst = [(1,0),(0,1),(2,1),(3,2)]
for t in range(int(input())):
 n = int(input())
 l = len(lst)
 while (n >= l):
  a = (lst[-1][0]+lst[-2][0]+lst[-3][0])%MOD
  b = (lst[-1][1]+lst[-2][1]+lst[-3][1])%MOD
  lst.append((a,b))
  l+=1
 print(lst[n][0],lst[n][1])
