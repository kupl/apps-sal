def paint_letterboxes(start, finish):
    boxes = ''.join([str(b) for b in range(start,finish+1)])
    return [ boxes.count(n) for n in '0123456789' ]
