def isDigit(string):
    try:
      float(string)
    except:
      string = False
    else:
      string = True
    return string
