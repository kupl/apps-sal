def check_for_factor(base,factor):
   
   check=False
   base=int(base)
   factor=int(factor)
  
   if factor > 0:
    if base%factor==0:
        check=True
    else :
        check=False
   else:
       check=False  
      
   return check   
      

