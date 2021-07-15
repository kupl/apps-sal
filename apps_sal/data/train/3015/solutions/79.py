

def get_issuer(number):
    

    n = str(number)
  
    if len(n)== 15:
    
        if n[0:2]== '34' or n[0:2]== '37':
        
  
              return "AMEX"
          
    if len(n)== 16 and  n[0:4] == '6011':
    
        return "Discover"
        
    if   len(n)== 13 or len(n)== 16:
    
        if n[0:1]== '4' :
    
            return "VISA"
        
    if len(n)== 16:
    
        if n[0:2]== '51' or n[0:2]== '52' or n[0:2]== '53' or n[0:2]== '54' or n[0:2]== '55':
        
  
              return "Mastercard"
    
    if len(n)==0:
    
        return "Unknown"
        
    else:
    
        return "Unknown"
        
        

