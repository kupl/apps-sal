for _ in range(eval(input())):
 n = eval(input())
 ar = list(map(int,input().split()))
 cnt = 0
 ans = []
 for i in range(n):
  if ar[i]==0:
   ans = [i+1] + ans
  else:
   ind = ans.index(ar[i])
   tmp = min(ind+1, len(ans)-ind-1)
   cnt += tmp
   ans = ans[:ind+1] + [i+1] + ans[ind+1:]
 print(cnt)
   

