def paint_letterboxes(start, finish):
    painted = "".join(map(str, range(start, finish+1)))
    return [painted.count(digit) for digit in "0123456789"]
