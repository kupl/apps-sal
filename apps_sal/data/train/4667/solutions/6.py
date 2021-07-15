def traffic_jam(main, ss):
    ret = list(main)
    for i,s in reversed(list(enumerate(ss))):
      for j,c in enumerate(s[::-1]): 
          ret.insert(i+j*2+1,c)
    return ''.join(ret[:ret.index('X')+1])
      
    

