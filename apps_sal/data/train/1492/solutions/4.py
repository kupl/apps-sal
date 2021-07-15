t = eval(input())
for i in range(t):
 n = eval(input())
 d = {'a':1000,'b':1000}
 for j in range(n):
  str = input()
  d['a']= min(str.count('a'),d['a'])
  d['b']= min(str.count('b'),d['b'])
 print(min(d['a'],d['b'])) 
