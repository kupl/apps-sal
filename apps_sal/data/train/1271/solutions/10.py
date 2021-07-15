from collections import Counter


a = int(input())
while a!=0:

 b = int(input())
 mylist = list()
 ev, od = 0, 0
 for i in range(b):
  c = int(input())

  fla=0

  for j in range(len(mylist)):


   if c==mylist[j]:
    print(ev,od)
    fla=1
    break
  if fla==1:
   continue

  temp = list()
  for j in range(len(mylist)):
   if c != mylist[j]:

    mylist.append(c^mylist[j])
    r = c^mylist[j]
    elem = mylist[j] ^ c
    
    if Counter(bin(elem)[2:])['1'] % 2 == 1:
     od += 1
    else:
     ev += 1
    mylist.append(r)
  mylist = list(set(mylist))
  mylist.append(c)


  elem = mylist[len(mylist)-1]

  if Counter(bin(elem)[2:])['1'] % 2 == 1:
   od += 1
  else:
   ev += 1



  print(ev,od)






 a-=1

