def set_alarm(em, va):
    if em == True and va == True:
        return False
    elif em == True and va == False:
        return True
    elif em == False and va == False:
        return False
    elif em == False and va == True:
        return False
    # Your code here
