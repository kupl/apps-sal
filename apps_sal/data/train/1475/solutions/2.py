from collections import Counter

def is_anagram(str1, str2):
 return Counter(str1) == Counter(str2)


s=input()
st=input()
s=s.split(" ")
i=0
c=""
for sr in s:
 i+=1
 if sr!=st and is_anagram(sr, st):
  c=c+str(i)

print("The antidote is found in " + c+ '.')
