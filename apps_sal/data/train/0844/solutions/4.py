tweets,clicks = list(map(int,input().split()))
openl = []

for i in range(clicks):
 action = input() .upper()
 if(action == "CLOSEALL"):
  openl = []
  print(0)
 else:
  if(action not in openl ):
   openl.append(action)
   print(len(openl))
  elif(action in openl):
   openl.remove(action)
   print(len(openl))
