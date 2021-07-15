# cook your dish here
for _ in range(int(input())):
 l = list(map(int, input().split()))
 s = l[0]
 w = []
 for i in range(1, len(l)):
  w.append(l[i])
 s1 = 0
 hit = 0
 if s>=w[0]+w[1]+w[2]:
  print(1)
 elif s>=w[0]+w[1]:
  hit += 2
  print(hit)
 elif s>=w[1]+w[2]:
  hit += 2
  print(hit)
 elif s==w[0]==w[1]==w[2]:
  print(3)



