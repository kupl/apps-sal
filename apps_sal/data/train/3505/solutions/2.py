def super_pad(string, width, fill=" "):
    if not fill or fill in '<^>':
        return string
    
    fill_len = width - len(string)
    
    # check padding mode
    if fill[0] == '>':
        l_pad, r_pad = 0, fill_len
    elif fill[0] == '^':
        l_pad, r_pad = (fill_len + 1) // 2, fill_len // 2
    else:
        l_pad, r_pad = fill_len, 0
    
    # if width < string length
    if fill_len < 0:
        return string[-l_pad if l_pad else None : r_pad if r_pad else None]
    
    # adjust the fill string
    if fill[0] in '<^>':
        fill = fill[1:]
    fill *= fill_len // len(fill) + 1
    
    return fill[:l_pad] + string + fill[:r_pad]
