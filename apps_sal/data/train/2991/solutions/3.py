def not_so_random(b,w):
    if b == 1 and w == 1:
        return 'Black'
    elif b == w:
        return 'White'
    elif b % 2 != 0:
        return 'Black'
    else:
        return 'White'
    
  
  # b & w => black
  # b & b => white
  # w & w => white

