def house_numbers_sum(inp):
    for i in range(len(inp)):
      if inp[i]==0:
        new=inp[:i]
        return sum(new)

