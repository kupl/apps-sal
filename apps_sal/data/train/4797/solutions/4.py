def shorter_reverse_longer(a,b):
  return a+b[::-1]+a if len(b)>len(a) else b+a[::-1]+b
