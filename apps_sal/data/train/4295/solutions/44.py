def balanced_num(number):
    st=str(number)
    if len(st)==1 or len(st)==2:
        return 'Balanced'
    elif len(st)>2:
        if len(st)%2==0:
            l=st[:int(len(st)/2)-1]
            r=st[int(len(st)/2)+1:]
        else:
            l=st[:int(len(st)/2)]
            r=st[int(len(st)/2)+1:]
    topl=lambda t: sum(int(i) for i in t)
    return 'Balanced' if topl(l)==topl(r) else 'Not Balanced'
