array_leaders=lambda a:[a[i] for i in range(len(a)) if a[i] > sum(a[i+1:])]
