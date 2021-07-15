# cook your dish here
t = int(input())
tt = 0
while tt < t :
 tt = tt + 1
 str = input()
 s, k = str.split()
 k = int(k)
 l = len(s)
 if l >= 14 and (2*l - k) > 26:
  print("NOPE")
 else :
  thisList = []
  j = 0
  while j < 26 :
   thisList.append(0)
   j = j + 1
  j = 0
  while j < l :
   a = str[j]
   b = ord(a)
   b = b - 97
   thisList[b] = 1
   j = j + 1
  str = ""
  j = 0
  i = 0
  while j < l:
   c = chr(i + 97)
   if thisList[i] == 0 :
    str = str + c
    j = j + 1
   elif k > 0:
    str = str + c
    j = j + 1 
    k = k - 1
   else :
    pass
   i = i + 1
  print(str) 
    
   
   
   
   
   
   
   
   
   
   
   
   
   

