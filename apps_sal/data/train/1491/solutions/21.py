abcd = input()
abcd = abcd.split()
abcd = list(map(int, abcd))
prod = 1
cnt = 0
for item in abcd:
 prod*=item
flo = prod**(0.5)
if int(flo) == flo:
 for i in range(3):
  for j in range(i+1,4):
   if abcd[i]*abcd[j] == flo:
    cnt = 1
    break
  if cnt==1:
   break
 if cnt == 1:
  print("Possible")
 else:
  print("Impossible")
else:
 print("Impossible")
