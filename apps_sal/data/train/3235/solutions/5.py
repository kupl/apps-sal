decompose_single_strand=lambda d:'\n'.join('Frame %d: %s'%(4-i,' '.join(map(''.join,zip(*[iter(' '*i+d+'  ')]*3))).strip())for i in(3,2,1))
