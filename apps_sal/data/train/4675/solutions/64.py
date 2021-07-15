def set_alarm(employed, vacation):
    if employed == vacation:
        return False
    elif employed == False and vacation == True:
        return False
    else:
        return True
