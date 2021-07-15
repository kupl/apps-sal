def list_depth(l):
    depths = [1]
    for elm in l:
        if isinstance(elm, list):
            depths.append(list_depth(elm) + 1)
    return max(depths)
