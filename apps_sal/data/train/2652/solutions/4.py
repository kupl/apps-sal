import re
def count_squares(shapes):
    squares = 0
    for i, j in enumerate(shapes):
        ind = [k for k, l in enumerate(j) if l == '+']
        for o in range(len(ind)):
            for p in range(o + 1, len(ind)):
                
                k, l = ind[o], ind[p]
                width = l - k
                if i + width >= len(shapes): continue
                
                upper_line = j[k:l + 1]
                left_line = ''.join([n[k] if k < len(n) else ' ' for n in shapes[i:i + width + 1]])
                right_line = ''.join([n[l] if l < len(n) else ' ' for n in shapes[i:i + width + 1]])
                bottom_line = shapes[i + width][k:l + 1]
              
                if all(re.fullmatch(r'\+[{}]*\+'.format(ch), seq) for seq, ch in \
                            zip([upper_line, left_line, right_line, bottom_line], '\+\- |\+ |\+ \-\+'.split())):
                    squares += 1
    return squares
