def correct(string):
    d ={'5':'S', '0':'O', '1':'I'}
    return ''.join([d.get(i,i) for i in string])
