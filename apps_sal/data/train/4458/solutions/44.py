def time_correct(t):
    import re
    if t==None:
        return None
    if t=="":
        return ""
    r = re.compile('\d\d:\d\d:\d\d')
    if r.match(t) == None:
        return None
    
    sec = int(t[6:])
    mnt = int(t[3:5])
    hr = int(t[0:2])
    
    if sec > 59:
        sec = sec % 60
        mnt += 1
    if mnt > 59:
        mnt = mnt % 60
        hr += 1
    hr = hr % 24
    
    return str(hr).zfill(2)+":"+str(mnt).zfill(2)+":"+str(sec).zfill(2)
