T = int(input())

for i in range(T):
 s = input()
 count = 0
 for j in range(len(s)):
  if(s[j].isdigit()):
   count += int(s[j])
 print(count)
