def split_without_loss(s,c):
    return [x for x in s.replace(c.replace('|',''),c).split('|') if x]
