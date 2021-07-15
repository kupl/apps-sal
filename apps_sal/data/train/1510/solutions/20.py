# cook your dish here
q = int(input())
for _ in range(q):
 
 arr = input()
 string = ["A","B","C","D","E","F","G","H","I","J"]
 cnt = 0
 for i in arr:
  
  if(len(string)==0):
   break
  #print(string)
  try:
   string.remove(i)
  except:
   pass
  
  cnt+=1
  
 print(cnt)
