longest=lambda s: max(''.join(c+' ' if c>d else c for c,d in (zip(s,s[1:]+' '))).split(), key=len)
