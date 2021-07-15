def converter(mpg):
    
    kpl = mpg * 1.609344 / 4.54609188 
    kpl = round(kpl * 100) / 100
    
    return kpl
    
     

