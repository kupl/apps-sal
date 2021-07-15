def draw(waves):
    m       = max(waves)
    rotHist = [ ('■'*v).rjust(m, '□') for v in waves ]
    return '\n'.join( map(''.join, zip(*rotHist)) )
