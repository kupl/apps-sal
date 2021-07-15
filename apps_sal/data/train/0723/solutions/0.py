def ans(l):
 s = ""
 i = 0
 while (i < len(l)):
  temp = l[i]
  k = temp[1]
  if (k != 0):
   s += str(temp[0]) + "x^" + str(k)
  else:
   s += str(temp[0])
  i += 1
  if (i < len(l)):
   s += " + "
 if (len(s) > 0):
  return s
 else:
  return "0"
 
test = int(input())
while (test != 0):
 test -= 1
 N = int(input())
 l = []
 while (N != 0):
  n,m = list(map(int,input().split()))
  if (m > 0):
   l += [[n*m,m-1]]
  N -= 1
 print(ans(l))

