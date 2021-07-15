def any_arrows(arrows):
    #your code here
    if not arrows :
        return False
        
    result = False
        
    for arrow in arrows:
        if ('damaged' not in arrow) or (arrow['damaged'] == False):
            result = result or True
        else:
            result = result or False
    return result
            
    

