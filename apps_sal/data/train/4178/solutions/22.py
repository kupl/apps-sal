min_sum=lambda a:a.sort()or sum(x*y for x,y in zip(a,a[::-1]))/2
