tc = int(input()) 

from sys import stdin

lines = stdin.readlines()
out = ""
i = 0
for line in lines:
 if i % 2 == 0:
  i += 1
  continue

  
 nn = list(map (int, line.split()))
 greatest = 0
 least = nn[0]
 diff = 0
 for n in nn:
  if n > least and n - least > diff:
   diff = n - least;
  elif n < least:
   least = n
   
 if diff > 0:
  out+=str(diff) + "\n"
 else:
  out += "UNFIT\n"
 i += 1
print(out)
