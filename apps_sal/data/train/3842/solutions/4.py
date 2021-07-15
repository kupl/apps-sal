def word_wrap(text, limit):
    r=[]
    l=''
    for w in text.split(' '):
        if len(l)+len(w)<=limit:
            l+=w+' '
        else:
            if len(w)<=limit:
                r.append(l.strip())
                l=w+' '
            else:
                if len(l.strip())==limit:
                    r.append(l.strip())
                    l=''
                l+=w
                while(len(l)>limit):
                    r.append(l[:limit])
                    l=l[limit:]
                l+=' '
    r.append(l.strip())
    return '\n'.join(r)
