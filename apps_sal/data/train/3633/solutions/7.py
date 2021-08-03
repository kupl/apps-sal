shuffle_it = si = lambda l, *a: l if not a or len(a[0]) == 0 else si([x if not i in a[0] else l[a[0][0]] if i == a[0][1] else l[a[0][1]] for i, x in enumerate(l)], *a[1:])
