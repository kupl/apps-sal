def array(s):
    if s=='':
        return None
    else:
        a=s.replace(' ','').replace(',',' ').split(' ')
        return None if len(a)<=2 else ' '.join(a[1:len(a)-1])
