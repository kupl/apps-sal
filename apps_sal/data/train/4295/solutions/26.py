def balanced_num(number):
    l = []
    brk = (len(str(number)) // 2)
    
    if len(str(number)) == 2 or len(str(number)) == 1:
        return "Balanced"    
    
    for i in str(number):
      l.append(int(i))
    
    if len(l) % 2 == 0:
      left = l[:brk-1]
      right = l[brk+1:]
      
      if sum(left) == sum(right):
        return "Balanced"
      else:
        return "Not Balanced"
      
    if len(l) % 2 != 0:
      left = l[:brk]
      right = l[brk+1:]
      
      if sum(left) == sum(right):
        return "Balanced"
      else:
        return "Not Balanced"
        
    pass
