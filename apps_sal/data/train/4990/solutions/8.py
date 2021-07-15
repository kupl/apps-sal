def solution(string, ending):
      if ending in string:
        if ending == '':  
            return True
        else:
            str1Arr = string.split(f'{ending}')
            if str1Arr[-1] == '':
              return True
            else:
              return False
      else:
          return False
