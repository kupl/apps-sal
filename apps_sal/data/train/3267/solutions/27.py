def well(x):
    '''
    if x.count('good') > 2: 
        return 'I smell a series!'
    elif x.count('good') > 0 < 3: 
        return 'Publish!'
    else:
        return 'Fail!'
        '''
    chk, l = x.count('good'), ['Fail!','Publish!','I smell a series!']
    return [l[0],l[1],l[1]][chk] if chk < 3 else l[2]
