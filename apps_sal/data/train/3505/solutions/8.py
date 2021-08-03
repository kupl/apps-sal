def super_pad(string, width, fill=" "):
    if not width:
        return ''
    if not fill:
        return string
    direction = fill[0]
    if direction in "<^>":
        fill = fill[1:]
    else:
        direction = "<"

    if direction == "<":
        return ((fill * width)[:max(0, width - len(string))] + string)[-width:]
    elif direction == ">":
        return (string + fill * width)[:width]
    else:
        left = (width - len(string) + 1) // 2
        right = (width - len(string)) // 2
        if right >= 0:
            left_padding = (fill * width)[:left]
            right_padding = (fill * width)[:right]
            return left_padding + string + right_padding
        else:
            return string[-left:right]

    return string
