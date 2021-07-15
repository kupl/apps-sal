def list_depth(l):
    temp=list(filter(lambda x:x in ('[',']'),str(l)))
    while temp[-1]==']':
        temp.pop()
    return temp.count('[')-temp.count(']')
