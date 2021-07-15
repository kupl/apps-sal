def get_num(n):
    holes=0
    for val in str(n):
      if val in '069':
        holes+=1
      if val=='8':
        holes+=2
    return holes
