def flip(ch): 
 return '1' if (ch == '0') else '0'
def FlipWithStart(str, expected): 
 flipCount = 0
 for i in range(len(str)):
  if (str[i] != expected): 
   flipCount += 1
  expected = flip(expected) 
 return flipCount
def minFlip(str):
 return min(FlipWithStart(str, '0'), FlipWithStart(str, '1'))
 
 
 
for _ in range(int(input())):
 n = int(input())
 s = input()
 print(minFlip(s))
