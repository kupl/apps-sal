triple_shiftian=lambda base,n: base[n] if n<len(base) else triple_shiftian(base+[4*base[-1]-5*base[-2]+3*base[-3]],n)
