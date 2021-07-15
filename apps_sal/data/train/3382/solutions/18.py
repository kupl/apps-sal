variable = 'abc'
def lowercase_count(strng):
      array = []
      for x in strng:
            index = ord(x[0])
            if 97 <= index <= 122 and index > 91 :
                  variableForArray = chr(index)
                  array.append(variableForArray)

            else :
                  continue
      return len(array)
