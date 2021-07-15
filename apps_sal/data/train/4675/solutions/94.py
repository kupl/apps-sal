def set_alarm(employed, vacation):
    s = ''
    if employed == True:
      if vacation == True:
        s = False
      else:
        s = True
    else:
      s = False
    return s
