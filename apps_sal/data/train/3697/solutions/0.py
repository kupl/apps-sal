def list_depth(l):
    depths = [1]
    for x in l:
        if isinstance(x, list):
            depths.append(list_depth(x) + 1)
    return max(depths)
