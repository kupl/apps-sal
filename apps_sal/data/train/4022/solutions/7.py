from itertools import groupby,islice

tr=str.maketrans('ABCDEFGIJKLMNOPQRSTUVXYZ','012301202245501262301202','HW')

def soundex(n):
    n=n.upper()
    ws=[]
    for w in n.split(' '):
        s=[]
        s=list(islice((vg[0] for i,vg in enumerate(groupby(w.translate(tr))) if vg[0]!='0' or i==0),4))
        if s[0]=='0' or s[0]==w[0].translate(tr):
            s[0]=w[0]
        else:
            s.insert(0,w[0])
        ws.append(''.join(s)[:4].ljust(4,'0'))
    return ' '.join(ws)

