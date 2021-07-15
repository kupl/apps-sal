decompose_single_strand=lambda s: "\n".join("Frame %s: %s" %(i+1," ".join(([s[:i]] if i else [])+[s[q:q+3] for q in range(i,len(s),3)])) for i in range(3))
