def find(seq):
  seq.sort()
  pattern = abs(seq[0]-seq[1])
  for i in range(len(seq)-1):
    if seq[i]!=seq[i+1]-pattern:
      return seq[i]+pattern
  

