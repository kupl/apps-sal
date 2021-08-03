def split_without_loss(s, split_p):
    to_find = split_p.replace('|', '')
    with_bar = s.replace(to_find, split_p)
    return [x for x in with_bar.split('|') if x != '']
