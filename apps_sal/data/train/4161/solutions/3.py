def rat_at(n):
    if not n: return (1,1)
    base = 0
    i = n + 1
    while i!=1:
      i= i>>1
      print(i)
      base+=1
    path = str(bin(n - 2**(base)  + 1 ))[2:]
    path = '0'*(base-len(path)) + path # buffer left side w/ 0s
    a=b=1
    path = [x=='1' for x in path]
    for p in path:
      if p: a += b
      else: b += a
    return (a,b)


def index_of(a, b):
    if a==b==1: return 0
    path = ""
    while a!=1 or b!=1:
      if a>b: # from the left, going right
        a-=b
        path = "1" + path
      else: # from the right, going left
        b-=a
        path = "0" + path
    base = 2**len(path) - 2  #int('1'*(count),2)
    addon = int(path,2)+1
    return base + addon
