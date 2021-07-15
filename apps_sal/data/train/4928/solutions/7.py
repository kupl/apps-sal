binRota=lambda a:[p for i,l in enumerate(a)for p in l[::1-i%2*2]]
