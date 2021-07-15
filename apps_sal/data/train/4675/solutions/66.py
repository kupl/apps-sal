def set_alarm(employed, vacation):
    if employed == False and vacation == True:
        return False
    else:
        return employed != vacation
