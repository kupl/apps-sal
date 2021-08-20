def array(string):
    strlist = string.split(',')
    finalstr = ' '.join(strlist[1:-1])
    return finalstr if finalstr != '' else None
