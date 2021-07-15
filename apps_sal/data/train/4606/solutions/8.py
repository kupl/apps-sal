from re import fullmatch
def valid_romans(arr):
    units = '((IV)|(IX)|(VI{0,3})|(I{1,3}))?'
    tens = '((XC)|(XL)|(LX{0,3})|X{1,3})?'
    hndr = '((CD)|(CM)|(DC{0,3})|C{1,3})?'
    ths = '(M{1,4}){0,1}'
    regex = ths + hndr  + tens + units 
    return [s for s in arr if fullmatch(regex,s) and 0 < len(s)]
