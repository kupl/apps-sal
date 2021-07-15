d = lambda a,b,c,d:abs(d-b)+abs(c-a)
optimum_location=lambda st,lc:'The best location is number {} with the coordinates x = {} and y = {}'.format(*min([sum(d(*n,i['x'],i['y']) for n in st),i['id'],i['x'],i['y']] for i in lc)[1:])
