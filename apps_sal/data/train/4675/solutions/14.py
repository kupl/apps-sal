def set_alarm(employed, vacation):
    if employed == vacation:
        return False
    return True if employed == True and vacation == False else False
    return False if employed == False and vacation == True else True
