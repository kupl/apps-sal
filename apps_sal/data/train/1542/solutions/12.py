#cook
pos_values = {"d" : 2, "t" : 3, "." : 1, "D" : 1, "T" : 1}
T = int(input())
for i in range(T):
 N = int(input())
 positions = input()
 values = input()
 
 list_of_values = []
 temp = 0
 prev = 0
 i = 0
 while i < len(values):
  if values[i] == " ":
   temp = int(values[prev : i])
   list_of_values.append(temp)
   prev = i+1
   i += 1
  else:
   i += 1
 
 temp = int(values[prev : i])
 list_of_values.append(temp)
 
 set_of_values = []
 
 for j in range(N-7):
  temp = 0
  for k in range(8):
   temp += list_of_values[k]*pos_values.get(positions[j+k])
  
  for k in range(8):
   if positions[j+k] == "D":
    temp *= 2
   elif positions[j+k] == "T":
    temp *= 3
  
  set_of_values.append(temp)
 
 max_num = 0
 for l in range(len(set_of_values)):
  max_num = max(max_num, set_of_values[l])
 
 print(max_num)
