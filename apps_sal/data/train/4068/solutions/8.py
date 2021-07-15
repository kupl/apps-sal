from math import ceil

def get_candy_position(n, r, c, candy):
    d = r * c
    boxes_cnt, boxes = ceil(n / d), []
    
    lst = [[i * c + j + 1 for j in range(c - 1, -1, -1)] for i in range(r - 1, -1, -1)]
    
    for i in range(boxes_cnt):
        boxes.append([i + 1, [[v + i * d if v + i * d <= n else 'x' for v in row] for row in lst]])
    
    bx = next((box for box in boxes if any(candy in b for b in box[1])), None)
    
    if not bx: return [-1, -1, -1]
    
    i = next(k for k, b in enumerate(bx[1]) if candy in b)
    j = bx[1][i].index(candy)
    
    return [bx[0], i, j]
