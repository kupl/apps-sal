
def correct(string):
  cor=''
  for leter in string:
    if leter =='1':
      cor+='I'
    elif leter=='5':
      cor+='S'
    elif leter=='0':
      cor+='O'
    else:
      cor+=leter
  return cor
