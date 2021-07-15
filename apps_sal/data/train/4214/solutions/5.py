def spin_solve(sentence):
    r=[]
    for w in sentence.split(' '):
        l=len(w.rstrip(',.'))
        if l>6 or w.lower().count('t')>=2:
            s=w[::-1]
            if not s[0].isalpha():
                s=s[1:]+s[0]
            r.append(s)
        elif l==2 or w[-1]==',':
            r.append(w.upper())
        elif l==1:
            r.append('0')
        else:
            r.append(w)
    return ' '.join(r)
