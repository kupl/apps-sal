t = eval(input())

def moneda(m):
 h = 1
 triange = []
 while m >= h:
  triange.append(h)
  m -= h 
  h += 1
 return len(triange)

triangulo = []
for i in range(t):
 n = eval(input())
 triangulo.append(n)

for i in triangulo:
 print(moneda(i))

