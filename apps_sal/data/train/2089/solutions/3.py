def n2b(n):
  b = bin(n)[2:]
  r = 10 - len(b)
  return list('0'*r + b)

def b2n(b):
  return int(''.join(b), 2)

def dump_encoded(s):
  ops = []
  op = '&'
  b = ''
  for i in range(10):
    if s[i] == '0':
      b += '0'
    else:
      b += '1'
  ops.append((op, b2n(b)))
  op = '|'
  b = ''
  for i in range(10):
    if s[i] == '1':
      b += '1'
    else:
      b += '0'
  ops.append((op, b2n(b)))
  op = '^'
  b = ''
  for i in range(10):
    if s[i] == 'y':
      b += '1'
    else:
      b += '0'
  ops.append((op, b2n(b)))

  print(len(ops))
  for op, n in ops:
    print(op,n)



# x, y, 0, 1

m = int(input())
ops = []
for i in range(m):
  op, n = input().split(' ')
  n = int(n)
  ops.append((op, n))


s = 1023
for i in range(len(ops)):
  op, n = ops[i]
  if op == '&':
    s = s & n
  elif op == '|':
    s = s | n
  elif op == '^':
    s = s ^ n
b1 = n2b(s)

s = 0
for i in range(len(ops)):
  op, n = ops[i]
  if op == '&':
    s = s & n
  elif op == '|':
    s = s | n
  elif op == '^':
    s = s ^ n
b2 = n2b(s)


g = ''
for k in range(10):
  if b1[k] == b2[k]:
    if b1[k] == '0':
      g += '0'
    else:
      g += '1'
  else:
    if b1[k] == '0':
      g += 'y'
    else:
      g += 'x'

dump_encoded(g)
