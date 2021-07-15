def convert_to_mixed_numeral(parm):
    p1,p2=map(int,parm.split('/'))
    if abs(p1)<p2 and p1!=0: return parm
    i=int(p1/p2)
    q=p1-i*p2
    return "{} {}/{}".format(i,abs(q),p2) if q!=0 else "{}".format(i)
