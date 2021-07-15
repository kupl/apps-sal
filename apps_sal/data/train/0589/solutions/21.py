for _ in range(int(input())):
 s = input()
 n = len(s)
 cnt = 0
 ans =0
 c =0
 for i in range(n):
  if s[i]=='.':
   cnt+=1
  else:
   if cnt > ans:
    c+=1
   ans = max(ans,cnt)
   cnt=0
 print(c)
