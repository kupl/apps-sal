def array(string):
    if len(string) <5:
      return None
    var =  string.split(',')
    var = var[1:-1]
    s = "";
    for i in var :
        s +=str(i)+" "
    if s[:-1] == '': 
      return None
    return s[:-1]
