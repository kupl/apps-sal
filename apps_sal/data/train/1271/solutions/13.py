
def countSetBits(n):
 count = 0
 while (n):
  count += n & 1
  n >>= 1
 return count



a = int(input())
while a!=0:

 b = int(input())
 mylist = list()

 for i in range(b):
  c = int(input())
  ev, od = 0, 0
  for j in range(len(mylist)):
   if c != mylist[j]:

    mylist.append(c^mylist[j])

  mylist.append(c)
  mylist = list(set(mylist))

  for j in range(len(mylist)):
   p = countSetBits(mylist[j])


   if p%2 == 0:
    ev+=1
   else:
    od+=1
  print(ev,od)






 a-=1

