import collections

while True:
 d = input().strip()
 myCounter = collections.Counter(d)
 flag = 1

 for x in list(myCounter.keys()):
  if myCounter[x] > 1:
   flag = 0
   break

 isAlp = sum([myCounter[x] for x in list(myCounter.keys()) if x.isalnum()])

 if flag and isAlp:
  print("Valid")
  break
 else:
  print("Invalid")

