# cook y
for i in range(int(input())):
 s=input()
 p="Bad"
 for i in range(len(s)-2):
  if '0' in s[i] and '1' in s[i+1] and '0' in s[i+2]:
   p="Good"
  if '1' in s[i] and '0' in s[i+1] and '1' in s[i+2]:
   p="Good"
 print(p)
  

