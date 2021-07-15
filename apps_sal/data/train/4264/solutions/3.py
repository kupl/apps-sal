def operation(a,b):
  return 0 if a==b else 1 + (operation(a//2, b) if a>b else operation(a, b//2))
