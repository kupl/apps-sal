n = int(input())
# this code only for 8 bits string and it isn't possible to more than 8 bits of     string 

# for i in range(n):
#      s = input()
#      subString1, subString2 = s[:4], s[4:]
#      rev = subString2[::-1]
#      print( 'uniform'  if(subString1 == rev)  else 'non-uniform')
  
for i in range(n):
 count = 0
 s = input()
 for i in range(1, len(s)):
  if(s[i-1] != s[i]):
   count += 1 
   
 if(s[0] != s[-1]): 
  count += 1 
 print("uniform" if(count <=2 ) else "non-uniform")

