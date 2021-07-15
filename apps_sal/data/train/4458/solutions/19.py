from re import match
def time_correct(t):
    if not t:return t
    if match("\d{2}:\d{2}:\d{2}",t):
        hour,minute,second=map(int,t.split(":"))
        m,second=divmod(second,60)
        minute+=m
        h,minute=divmod(minute,60)
        hour=(hour+h)%24
        return f"{hour:0>2d}:{minute:0>2d}:{second:0>2d}"
