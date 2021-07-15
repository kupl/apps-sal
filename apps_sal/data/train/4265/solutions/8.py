tops=lambda m,n=1: (lambda q: "" if q>len(m) else tops(m,n+1)+m[q])(2*n*n-n)
