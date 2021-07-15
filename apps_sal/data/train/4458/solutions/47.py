def time_correct(t):
    if not t:
        return t
    try:
        h,m,s=map(int,t.split(':'))
        if s>=60:
            s-=60
            m+=1
        if m>=60:
            m-=60
            h+=1
        h%=24
        return '{:02d}:{:02d}:{:02d}'.format(h,m,s)
    except:
        return None
