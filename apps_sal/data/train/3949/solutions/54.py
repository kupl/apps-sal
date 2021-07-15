import math

def calculate_tip(amount, rating):
    
    rating=rating.lower()
    
    result_2="Rating not recognised"
    result=-1
    
    if rating=="poor":
       result=amount*0.05
    elif rating== "good":
       result=amount*0.1
    elif rating== "great":   
       result=amount*0.15
    elif rating== "excellent":   
       result=amount*0.2
    elif rating=="terrible":
       result=0
    
    
  
    
    if result==-1:
       result=result_2
    
    if rating not in ("poor","excellent","great","good","terrible") :
        return 'Rating not recognised'
    else:
        return math.ceil(result)
