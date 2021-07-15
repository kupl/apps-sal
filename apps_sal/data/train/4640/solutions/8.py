int_diff=lambda a,n:a.sort()or sum(x-y==n for i,x in enumerate(a)for y in a[:i])
