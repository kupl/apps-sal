l, r = [], []
for i, c in enumerate(input()):
  if c == 'l':
    r += [str(i + 1)]
  else:
    l += [str(i + 1)]
r.reverse()
print('\n'.join(l + r)) 

