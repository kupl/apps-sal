def build_square(blocks):
    a = 4
    b = blocks.count(1)
    c = blocks.count(2)
    d = blocks.count(3)
    e = blocks.count(4)
    a -= e
    if a <= 0:
        return True
    while b > 0 and d > 0:
        b-=1
        d-=1
        a-=1
    while c > 0 and b > 1:
        b-=2
        c-=1
        a-=1
    while b > 3:
        b-=4
        a-=1
    while c > 1:
        c-=2
        a-=1
    if a <= 0:    
      return True
    else:
      return False
     
            
            
    
        

