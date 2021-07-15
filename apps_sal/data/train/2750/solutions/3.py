m=[0]
for _ in range(1000): m.append(1+sum(m[j+1] for j in range(len(m)//2)))

def make_sequences(n):
  return m[n]
