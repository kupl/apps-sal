t = int(input())

for _ in range(t):
 s, w1, w2, w3 = [int(x) for x in input().split()]
 
 if(w1+w2+w3 <= s):
  print(1)
 elif(w1+w2 <= s or w3+w2 <= s):
  print(2)
 else:
  print(3)
