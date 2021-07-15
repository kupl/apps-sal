def getInput():
 N_k = input().split()
 N =int(N_k[0])
 k =int(N_k[1])
 list = []
 output = []
 count = 0
 for i in range(0,k):
  val = input()
  if(val!="CLOSEALL"):
   val=val.split()
   val = int (val[1])
   if val not in list:
    count= count +1
    list.append(val)
   else:
    list.remove(val)
    count= count -1
  else:
   count =0
   while len(list) > 0: 
    list.pop()
  output.append(count)
 for each in output:
  print(each)
getInput()
