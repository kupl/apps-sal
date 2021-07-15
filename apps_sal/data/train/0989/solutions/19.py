# cook your dish here
try:
 t = int(input())
 for _ in range(t):
  nums = list(map(int,input().split()))
  X,Y,K = nums[0],nums[1],nums[2]
  s = X+Y
  if s%K==0:
   if s%2==0:
    print('Chef')
    continue
   else:
    print('Paja')
  else:
   ans = s//K
   if ans%2==0:
    print('Chef')
   else:
    print('Paja')
except:
 pass
    

