import re
def interweave(s1, s2):
    z=''.join([x+y for x,y in zip(s1,s2+' ')])[:-1]
    return re.sub(r'[0-9]','',z)

