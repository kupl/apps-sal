def split_without_loss(s,a):
    aa=a.split("|")
    ss=s.replace(aa[0]+aa[1], a).split("|")
    return [i for i in ss if i]
