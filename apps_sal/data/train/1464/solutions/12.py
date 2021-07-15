for _ in range(int(input())):
 yy,mm,dd = map(int, input().split(':'))
 if mm in [1,3,5,7,8,10,12]:
  ans = ((31-dd)//2)+1
 elif mm in [4,6,9,11]:
   ans = ((61 - dd) // 2) + 1
 else:
  if (yy % 4 == 0 and yy % 100 != 0) or yy % 400 == 0:
   ans = ((29 - dd) // 2) + 1
  else:
   ans = ((28+31 - dd) // 2)+1
 print(ans)
