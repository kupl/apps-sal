def super_pad(s, width, fill=" "):
    padding = width - len(s)
    if width == 0:
        return ''

    def _left_pad():
        if padding >= 0:
            return (fill * padding)[:padding] + s
        return s[-width:]

    def _right_pad():
        if padding >= 0:
            return s + (fill * padding)[:padding]
        return s[:width]

    def _center_pad():
        right = padding // 2
        left = padding - right
        if padding >= 0:
            return (fill * left)[:left] + s + (fill * right)[:right]
        return s[-left:right]

    if fill and fill[0] == '>':
        fill = fill[1:]
        return _right_pad()
    if fill and fill[0] == '^':
        fill = fill[1:]
        return _center_pad()
    if fill and fill[0] == '<':
        fill = fill[1:]
    return _left_pad()
