#read input
cases = int(input())
caselist = []
for i in range(0, cases):
 caselist.append(input())

#iterate each case
for j in range(0, cases):

 #current case's parameters:
 current_input = caselist[j].split(' ')
 bots = int(current_input[0])
 switch = int(current_input[1])

 #generate botlist and cakelist
 botlist = list(range(switch, bots)) + list(range(0, switch))
 cakelist = [False] * bots


 counter = 0
 index = 0
 for i in range(0,bots):
  if cakelist[index] == False:
   cakelist[index] = True
   counter += 1
   index = botlist[index]
  else:
   break

 if counter == bots:
  print("Yes")
 else:
  print("No", counter)
  

 

