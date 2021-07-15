def palSub(s,n,isPal):
 for gap in range(n):
  for i in range(n-gap):
   j = i + gap
   if(gap == 0):
    isPal[i][j] = 1
   elif(gap == 1):
    isPal[i][j] = 1 if(s[i] == s[j]) else 0
   else:
    isPal[i][j] = 1 if(s[i] == s[j] and isPal[i+1][j-1]) else 0
 return isPal
def case1(n,isPal,c1):
 for i in range(n):
  for j in range(i,n):
   if(i == j):
    c1[i][j] = 1
   else:
    c1[i][j] = c1[i][j-1] + isPal[i][j]
 return c1
def case2(n,isPal,c2):
 for j in range(n-1,-1,-1):
  for i in range(j,-1,-1):
   if(i == j):
    c2[i][j] = 1
   else:
    c2[i][j] = c2[i+1][j] + isPal[i][j]
 return c2
def getSub(s,n,c1,c2,res):
 for gap in range(n):
  for i in range(n-gap):
   j = i + gap
   if(gap == 0):
    res[i][j] = 0
   elif(gap == 1):
    res[i][j] = 1 if(s[i] == s[j]) else 0
   elif(s[i] == s[j]):
    res[i][j] = 1 + c1[i+1][j-1] + c2[i+1][j-1] + res[i+1][j-1]
 return res
def __starting_point():
 s = input()
 n = len(s)
 isPal = [[0 for x in range(n)]for y in range(n)]
 isPal = palSub(s,n,isPal)
 c1 = [[-1 for x in range(n)]for y in range(n)]
 c2 = [[-1 for x in range(n)]for y in range(n)]
 c1 = case1(n,isPal,c1)
 c2 = case2(n,isPal,c2)
 res = [[0 for x in range(n)]for y in range(n)]
 res = getSub(s,n,c1,c2,res)
 mycount = 0
 for i in range(n):
  for j in range(n):
   mycount += res[i][j]
 print(mycount)
__starting_point()
