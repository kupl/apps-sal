t = int(input())
while t:
 string = list(input())
 ans = 0
 for char in string:
  if ord(char) >= 48 and ord(char) <= 57:
   ans += ord(char) - 48 
 print(ans)
 t -= 1 
