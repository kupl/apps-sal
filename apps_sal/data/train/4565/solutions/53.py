def replace_dots(str):
    for i in range(len(str)):
      if str[i] =='.':
        str=str.replace(str[i],'-')
    return str
