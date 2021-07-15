def split_without_loss(s, split_p):
    return [i for i in s.replace(split_p.replace('|', ''), split_p).split('|') if i]
