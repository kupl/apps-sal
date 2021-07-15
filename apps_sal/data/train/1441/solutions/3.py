# cook your dish here
for t in range(int(input())):
 n, k = map(int, input().split())
 a = list(map(int, input().split()))
 x = list(map(int, input().split()))
 
 wv = max(a)
 wvi = a.index(wv)
 
 dp = [False]*n
 dp[wvi] = True
 # print(wvi)
 for i in range(wvi-1, -1, -1):
  for j in x:
   if (i+j)>n:
    continue
   if (i+j)>wvi:
    dp[i] = True
   elif dp[i+j]==False:
    # print(i, j)
    dp[i] = True
    break
 # print(dp)
    
 if dp[0]:
  print("Chef")
 else:
  print("Garry")
