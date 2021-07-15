def split_without_loss(s, split_p):
    # maybe breaks the input modification rule
    return s.replace(split_p.replace('|', ''), split_p).lstrip('|').rstrip('|').split('|')
