# your code goes here

t = int(input())
for i in range(t):
 n = int(input())
 words = input().split()
 ans = ''
 for i in range(0, len(words[0])):
  for j in range(i+1, len(words[0])+1):
   found = True
   for word in words[1:]:
    if not words[0][i:j] in word:
     found = False
     break
   if found:
    if len(ans) == len(words[0][i:j]) and ans > words[0][i:j]:
     ans = words[0][i:j]
    elif len(ans) < len(words[0][i:j]):
     ans = words[0][i:j]
 print(ans)
    

