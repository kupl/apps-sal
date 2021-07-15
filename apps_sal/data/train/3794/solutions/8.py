nth_smallest = lambda a,n: None if len(set(a))<n else list(sorted(set(a)))[n-1]
