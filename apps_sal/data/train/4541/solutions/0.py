def array_operations(a, n):
  li = []
  for i in range(n):
        m = max(a)
        a = [m-i for i in a] 
        if a in li:
            if not n & 1 : return li[-1]
            return a
        li.append(a)
  return a
