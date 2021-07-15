def findHeight():
 tests = int(input())
 for t in range(tests):
  n = int(input())
  sumd = 0
  res = 0
  for i in range(1, n+1):
   sumd+=i
   if sumd == n:
    res = i
    break
   elif sumd > n:
    res = i-1
    break
  print(res)

findHeight()



