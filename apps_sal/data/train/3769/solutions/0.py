from collections import deque
import re

TOKENIZER = re.compile(r'(R+|F+|L+)(\d*)')

def execute(code):
    
    pos, dirs = (0,0), deque([(0,1), (1,0), (0,-1), (-1,0)])
    seens = {pos}
    
    for act,n in TOKENIZER.findall(code):
        s,r = act[0], int(n or '1') + len(act)-1
        
        if s == 'F':
            for _ in range(r):
                pos = tuple( z+dz for z,dz in zip(pos, dirs[0]) )
                seens.add(pos)
        else:
            dirs.rotate( (r%4) * (-1)**(s == 'R') )
    
    miX, maX = min(x for x,y in seens), max(x for x,y in seens)
    miY, maY = min(y for x,y in seens), max(y for x,y in seens)
    
    return '\r\n'.join( ''.join('*' if (x,y) in seens else ' ' for y in range(miY, maY+1)) 
                        for x in range(miX, maX+1) )
