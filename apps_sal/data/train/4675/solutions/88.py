def set_alarm(employed, vacation):
    # Your code here
    if employed:
        if vacation == False:
            return True
        if vacation:
            return False
    else:
        return False
