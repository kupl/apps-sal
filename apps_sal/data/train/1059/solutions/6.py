size = int(input())
array = []

for x in range(size):
 array.append(int(input()))
 
diff = 0 

if size < 1600 :
 for i in range(size):
  for j in range(i + 1, size):
   if array[i]%array[j] > diff :
    diff = array[i]%array[j]
else :
 m1 = max(array)
 array.pop(array.index(m1))
 m2 = max(array)
 diff = m2%m1
 
print(diff)
