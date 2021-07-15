def christmas_tree(height):
    if height < 3:
        return ""
    result = []
    for i in range(height // 3):
        w = 1 + 2 * i
        result.append("*" * w)        
        result.append("*" * (w + 2))
        result.append("*" * (w + 4))
    result.append("###")
    l = len(result[-2])
    return "\r\n".join([line.center(l).rstrip() for line in result])
