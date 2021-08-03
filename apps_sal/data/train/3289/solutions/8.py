def motif_locator(s, m): return sorted(list({s.find(m, e) + 1 for e, i in enumerate(range(len(s))) if s.find(m, e) != -1}))
