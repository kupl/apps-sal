def array(string):
    x = string.split(',')
    if len(x) <= 2 :
        return None
    else:
        x.pop()
        x.pop(0)
        return ' '.join(x)
print((array('1,2,3,4,5,6,7,8,9')))

