t = int(input())
for _ in range(t):
 n = int(input())
 a = [(bin(int(x))[2:][::-1]+("0")*32)for x in input().split()]
 res = ""
 mysum = 0
 for i in range(32):
  mycount = 0
  for j in range(n):
   if(a[j][i] == "0"):
    mycount += 1
  if(mycount == n):
   break
  if(mycount > (n//2)):
   res += "0"
   mysum += (n-mycount)*int(pow(2,i))
  else:
   res += "1"
   mysum += mycount*int(pow(2,i))
 print(mysum)
