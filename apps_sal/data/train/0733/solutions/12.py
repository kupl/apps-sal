# cook your dish he
t = int(input())
while t>0:
 t-=1
 n = int(input())
 str = input()
 s = []
 for i in range(n):
  s.append(ord(str[i]))
 a = min(s)
 print(chr(a))
