covered_pawns=lambda p:len(set(p)&set.union(*({chr(ord(c)+b)+chr(ord(r)+1)for b in(-1,1)}for c,r in['  ']+p)))
