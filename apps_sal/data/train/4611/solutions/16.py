def animals(heads, legs):
    y = legs/2 - heads
    x = heads - y
    return (x,y) if all([int(x)==x, int(y)==y, x>=0, y>=0]) else "No solutions"
