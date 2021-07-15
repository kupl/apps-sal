ncases = int(input())

for cases in range(ncases):
 items = int(input())
 pricelist = list( map( int, input().split()))
 intended = 2000
 if pricelist.count(1000) >= 2:
  print("Accepted")
  continue

 accepted = False
 for i in pricelist:
  if i != 1000 and intended - i in pricelist:
   accepted =True
  
 if accepted:
  print("Accepted")
 else:
  print("Rejected")

 

