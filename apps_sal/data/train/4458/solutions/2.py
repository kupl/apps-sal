def time_correct(t):
    try:
        if t=="":
            return ""
        if len(t)!=8:
            return None
        h,m,s=[int(x) for x in t.split(":")]
        if s>=60:
            s-=60
            m+=1
        if m>=60:
            m-=60
            h+=1
        if h>=24:
            h=h%24
        return '%02d:%02d:%02d'%(h,m,s)
    except:
        return None
