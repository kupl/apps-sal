import math

def countSetBits(n):
 count = 0
 while (n):
  n &= (n - 1)
  count += 1

 return count

a = int(input())
while a!=0:
 mylist = list()
 b= int(input())
 count_even = 0
 count_odd = 0
 for j in range(b):

  c = int(input())
  t=0
  for i in range(len(mylist)):
   if(mylist[i] == c):
    t=1
    break
  if(t == 0):
   for i in range(len(mylist)):
    if(mylist[i] != c):
     p = mylist[i]^c
     q = math.log2(p)
     if(q == int(q)):
      count_odd+=1
     else:
      if(countSetBits(p)%2 == 0):
       count_even+=1
      else:
       count_odd+=1
     mylist.append(p)
    else:
     mylist.append(c)
   mylist.append(c)
   p = math.log2(c)
   if(p == int(p)):
    count_odd+=1
   else:
    if(countSetBits(c)%2 ==0):
     count_even+=1
    else:
     count_odd+=1
  print(count_even,count_odd)






 a-=1




