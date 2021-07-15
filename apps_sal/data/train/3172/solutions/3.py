TOME = {0:'▇', 1:'＿', 'K':'♚', 'Q':'♛', 'R':'♜', 'B':'♝', 'N':'♞', 'P':'♟', 'k':'♔', 'q':'♕', 'r':'♖', 'b':'♗', 'n':'♘', 'p':'♙'}

def parse_fen(s):
    bd,color,*_ = s.split()
    bd = [formatRow(row, x&1) for x,row in enumerate(bd.split('/'))]
    if color=='b':
        bd = (r[::-1] for r in reversed(bd))
    return '\n'.join(bd) + '\n'

def formatRow(row,p):
    out = ''.join( TOME[c] if not c.isdigit() else 'x'*int(c) for i,c in enumerate(row))
    return ''.join(c if c!='x' else TOME[p^i&1] for i,c in enumerate(out))
