min_sum=lambda a:sum(x*y for x,y in zip(list(sorted(a)[:len(a)//2]),list(sorted(a,reverse=True)[:len(a)//2])))
