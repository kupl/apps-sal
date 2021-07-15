kontti=lambda s:' '.join((lambda i:i<len(w)and'ko'+w[i+1:]+'-'+w[:i+1]+'ntti'or w)(min(i for i,c in enumerate(w+'a')if c in'aeiouyAEIOUY'))for w in s.split())
