factorials=[1]

for x in range(1,201):
 factorials.append(factorials[x-1]*x)
 
x=int(input())

for x in range(x):
 n=int(input())
 print(factorials[n])
