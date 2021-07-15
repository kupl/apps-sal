# cook your dish here
t = int(input())
for _ in range(t):
 s = input()
 x = s.count('0')
 y = s.count('1')
 if (len(s)%2 == 1 or x == 0 or y == 0):
  print(-1)
 else:
  print(abs(x-y)//2)
