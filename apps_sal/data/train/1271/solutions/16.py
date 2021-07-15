import math

def countSetBits(i):

 i = i - ((i >> 1) & 0x55555555)
 i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
 return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24
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




