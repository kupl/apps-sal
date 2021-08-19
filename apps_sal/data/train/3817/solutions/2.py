def split_without_loss(s, split_p):
    result = []
    pipe_index = split_p.find('|')
    split_p = split_p.replace('|', '')
    split_index = s.find(split_p)
    begin = 0
    while split_index != -1:
        if split_index + pipe_index != 0:
            result.append(s[begin:split_index + pipe_index])
        begin = split_index + pipe_index
        split_index = s.find(split_p, split_index + len(split_p))
    if begin != len(s):
        result.append(s[begin:])
    return result
