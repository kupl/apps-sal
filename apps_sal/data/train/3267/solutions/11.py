def well(x):
    y=0
    
    for c  in x:
        if c=="good":
            y=y+1
            
    if y==0:
        return 'Fail!'

    if y > 2:
        return 'I smell a series!'
        
        
    return 'Publish!'
    
   #  'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

