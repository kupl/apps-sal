def black_and_white(height, width, compressed):
    (res, left, i, color) = ([], 0, 0, 0)
    for h in range(height):
        (tot, tmp) = (0, [])
        if color == 1:
            tmp.append(0)
        while tot < width and i < len(compressed):
            if left:
                if left <= width:
                    tmp.append(left)
                    (tot, left, color) = (left, 0, 1 - color)
                else:
                    tmp.append(width)
                    (tot, left) = (width, left - width)
            else:
                (i, val) = (i + 1, compressed[i])
                if tot + val <= width:
                    tmp.append(val)
                    (tot, color) = (tot + val, 1 - color)
                else:
                    tmp.append(width - tot)
                    (tot, left) = (width, tot + val - width)
        if len(tmp) % 2:
            tmp.append(left if h == height - 1 else 0)
        res.append(tmp)
    return res
