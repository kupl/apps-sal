def nondecdigits(s):
 m = len(s); 
 a = [0] * m; 
 for i in range(m):
  a[i] = ord(s[i]) - ord('0'); 
 level = m - 1;
 for i in range(m - 1, 0, -1):
  if (a[i] < a[i - 1]):
   a[i - 1] -= 1;
   level = i - 1;
 if (a[0] != 0):
  for i in range(level + 1):
   print(a[i], end="");
  for i in range(level + 1, m):
   print("9", end="");
 else:
  for i in range(1, level):
   print(a[i], end="");
  for i in range(level + 1, m):
   print("9", end="");
x=int(input())
for i in range(x):
 y=int(input())
 nondecdigits(str(y))
 print()
