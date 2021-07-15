capitalize=lambda s:[''.join(chr(ord(c)-i%2*32)for i,c in enumerate(s,n))for n in[1,0]]
