def set_alarm(employed, vacation):
    
    if vacation == True:
        return False
        
    if employed == False and  vacation == False:
        return False
        
    else:
        return True
