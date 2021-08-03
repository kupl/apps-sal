import re


class Me(object):
    def __init__(self): self.x, self.y, self.dx, self.dy = 0, 0, -1, 0
    def move(self, n): self.x += n * self.dx; self.y += n * self.dy
    def back(self): self.dx *= -1; self.dy *= -1
    def turn(self, d): self.dx, self.dy = (self.dy * (-1)**(d == 'l'), 0) if self.dy else (0, self.dx * (-1)**(d == 'r'))
    def where(self): return [self.x, self.y]
    def __str__(self): return f'x,y={self.x},{self.y} (dx,dy={self.dx},{self.dy})'


me = Me()


def i_am_here(path):
    for v in re.findall(r'\d+|.', path):
        if v in 'RL':
            me.back()
        elif v in 'rl':
            me.turn(v)
        else:
            me.move(int(v))
    return me.where()
