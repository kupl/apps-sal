import re
# def slogans(p,r):
#     if not r:return 0
#     n=0
#     while not r.startswith(p[n:]):n+=1
#     return 1+slogans(p,r.replace(p[n:],'',1))
def slogans(p,r):
    if not r:return 0
    return 1+slogans(p,r.replace(re.search(r'.+?(.+)\s\1.*',' '.join([p,r])).group(1),'',1))
