s = 'abcde123fghij456klmno789pqrst.@0uvwxyz_/'
dx = lambda c1, c2 : abs(s.index(c1)%8  - s.index(c2)%8)
dy = lambda c1, c2 : abs(s.index(c1)//8 - s.index(c2)//8)
d  = lambda c1, c2 : 1 + dx(c1, c2) + dy(c1, c2)

def tv_remote(word, r=0):
    if r==0         : return tv_remote(word, d('a', word[0]))
    if len(word)==1 : return r
    else            : return tv_remote(word[1:], r+d(word[1], word[0]))
