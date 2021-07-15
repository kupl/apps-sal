f=[0,1,2,2]
for i in range(4,1001):
    f.append(1+sum(f[:i//2+1]))
def make_sequences(n):
  return f[n]
