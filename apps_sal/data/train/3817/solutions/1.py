import re

def split_without_loss(s, m):
    r,iM  = m.replace('|',''), m.index('|')
    out,i,j = [],0,0
    while 1:
        j = s.find(r,j)
        if j==-1:
            if i<len(s): out.append(s[i:])
            break
        if i<j+iM: out.append(s[i:j+iM])
        i,j = j+iM,j+len(r)
    return out
