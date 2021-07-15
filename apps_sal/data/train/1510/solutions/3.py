# cook your dish here
try:
 
 l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
 t = int(input())
 
 for i in range(t):
  x = list(input())
  x = [i for i in x if i in l]
  print(len(x))
except:
 pass
