def split_without_loss(s, split_p):
    return s.replace(split_p.replace('|', ''), split_p).lstrip('|').rstrip('|').split('|')
