# cook your dish here
m , n = input().split()
for i in range(int(n)):
 if m[-1] == '0':
  m = m[:len(m)-1]
 else:
  b = int(m[-1])-1
  m = m[:len(m)-1]+str(b)
print(int(m))

