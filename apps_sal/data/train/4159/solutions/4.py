from itertools import zip_longest
poly_multiply=lambda a,b:[sum(i) for i in zip_longest(*[[0]*i+[j*k for k in a] for i,j in enumerate(b)],fillvalue=0)] if a else []
