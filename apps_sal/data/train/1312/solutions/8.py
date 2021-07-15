t = int(input())
spoon = "spoon"
while t>0:
 t -= 1
 x, y = list(map(int, input().split(" ")))
 inp = []
 done = False
 for i in range(x):
  inp.append(input().lower())
 if y>4:
  for i in range(x):
   if inp[i].find(spoon) != -1:
    print("There is a spoon!")
    done = True
    break
  if done:
   continue
 if x>4:
  for i in range(y):
   temp = ""
   for j in range(x):
    temp += inp[j][i]
   if temp.find(spoon) != -1:
    print("There is a spoon!")
    done = True
    break
  if done:
   continue
 print("There is indeed no spoon!")
