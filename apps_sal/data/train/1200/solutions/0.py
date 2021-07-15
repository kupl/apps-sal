def checkValidity(s):
 count = 0
 previous = ""

 for x in s:
  if count == 0:
   previous = x
   count += 1
  elif count == 1:
   count = 0
   if previous == x:
    return "no"

 return "yes"

t = int(input())

for _ in range(t):
 s = input()
 print(checkValidity(s))

