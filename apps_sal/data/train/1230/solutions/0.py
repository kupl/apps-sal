dic = {}
#num = "1"
#def tonum(num):
#   res=0
#   for i in range(len(num)):
#       res = 2*res + int(num[i])
#   return res

#for i in range(64):
#   number = tonum(num)
#   dic[num] = []
#   num = num+"0"

n = int(input())
flag=0
if n >= 68:
 inp = input()
 print("Yes")
else:
 inp = [int(x) for x in input().split()]
 for i in range(len(inp)-1):
  for j in range(i+1,len(inp)):
   xor = inp[i]^inp[j]
   if xor in list(dic.keys()):
    for pair in dic[xor]:
     (x,y) = pair
     if x != i and y!=j and x!=j and y!=i:
      flag = 1
      break

    dic[xor].append((i,j))
   else:
    dic[xor] = []
    dic[xor].append((i,j))
   if flag is 1:
    break
  if flag is 1:
   break

 if flag is 1:
  print("Yes")
 else:
  print("No")
 
 

