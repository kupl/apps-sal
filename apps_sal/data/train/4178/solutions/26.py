min_sum=lambda arr: (lambda s: sum(v*s[-i-1] for i,v in enumerate(s[:len(s)//2])))(sorted(arr))
