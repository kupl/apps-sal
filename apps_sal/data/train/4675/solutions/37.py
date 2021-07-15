def set_alarm(employed, vacation):
    if employed==True and vacation==True:
        alarma=False
    elif employed==False and vacation==True:
        alarma=False
    elif employed==False and vacation==False:
        alarma=False
    elif employed==True and vacation==False:
        alarma=True
    return alarma

