clamp  = lambda moves, w, h: {(x, y) for x, y in moves if 0 <= x < w and 0 <= y < h}
knight = lambda x, y: {(x+u, y+v) for u in range(-2, 3) for v in range(-2, 3) if u*u + v*v == 5}
rook   = lambda x, y, w, h: {(x, v) for v in range(h)} | {(u, y) for u in range(w)} - {(x, y)}
bishop = lambda x, y, w, h: {(x+d*k, y+k) for d in (-1,1) for k in range(-max(x, y), max(w-x, h-y))} - {(x, y)}

def search_triangle(x, y, w, h):
    return sum(
        len(rook(x, y, w, h) & clamp(bishop(u, v, w, h), w, h)) +
        len(rook(u, v, w, h) & clamp(bishop(x, y, w, h), w, h))
        for u, v in clamp(knight(x, y), w, h)
    )

def chess_triangle(h, w):
    wm, hm = min(6, w), min(6, h)
    return (
        sum(search_triangle(min(x, wm-x-1), min(y, hm-y-1), w, h) for x in range(wm) for y in range(hm))
        + max(0, w-6) * sum(search_triangle(3, min(y, hm-y-1), w, h) for y in range(hm))
        + max(0, h-6) * sum(search_triangle(min(x, wm-x-1), 3, w, h) for x in range(wm))
        + max(0, h-6) * max(0, w-6) * search_triangle(3, 3, w, h)
    )
