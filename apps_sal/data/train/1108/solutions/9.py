storage = list(input().split(' '))
count = 0
for j in range(int(storage[0])):
 n = list(input().split(' '))
 flag1 = False
 flag2 = False
 sum = 0
 for k in range(int(storage[2])):
  sum += int(n[k])
 if int(storage[1]) <= sum:
  flag1 = True
 if int(n[-1]) <= 10:
  flag2 = True
 if flag1:
  if flag2:
   count+=1
print(count)

