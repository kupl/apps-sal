t = eval(input())

for i in range(t):
 n = eval(input())
 a = list(map(int, input().split()))
 cnt = 2
 cnt1 = 2
 ll = len(a)
 if ll < 3:
  cnt1 = ll
 else:
  for j in range(2,ll):
   if a[j-1] + a[j-2] == a[j]:
    cnt += 1
    cnt1 = max(cnt1, cnt)
   else:
    cnt1 = max(cnt1, cnt)
    cnt = 2
 print(cnt1) 
