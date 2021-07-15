def house_numbers_sum(inp):
    n = 0
    for i in inp:
       if i==0:
          return n
       else:
          n = n+i
    return n
