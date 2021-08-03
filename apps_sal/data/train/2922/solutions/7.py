crap = lambda g, b, c, l=[]: l.clear() or [l.extend(e)for e in g][0] or ['Clean', 'Cr@p', 'Dog!!'][('D' in l) * 2 or l.count('@') > b * c]
