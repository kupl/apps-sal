sierpinski=lambda n,pr=['*'],sp=3:sierpinski(n-1,pr+[(j+(' '*len(pr[-1-i]))+j)for i,j in enumerate(pr)],sp*2+1)if n else'\n'.join([i.center(sp//2)for i in pr])
