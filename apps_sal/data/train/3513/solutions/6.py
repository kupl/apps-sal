def folding(a,b):
  #coding and coding..
    n=1
    while a > b:
        a_new = a-b
        a = max(a_new,b)
        b = min(a_new,b)
        n+=1
    return n

