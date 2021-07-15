def Dragon(n, Curve='Fa'):
  if type(n)!=int or n%1!=0 or n<0: return '' 
  
  elif n==0: 
      return Curve.replace('a','').replace('b','')
  else: 
      #now need to add an extra step where we swap out a dn b because otherwise the replace will affect the outcome. ie the replaces are not concurrent
      return Dragon(n-1, Curve.replace('a','c').replace('b','d').replace('c','aRbFR').replace('d', 'LFaLb') )
