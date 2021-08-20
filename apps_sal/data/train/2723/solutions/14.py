average_string = lambda s, d='zero one two three four five six seven eight nine'.split(): (lambda l: set() < set(l) <= set(d) and d[sum(map(d.index, l)) // len(l)] or 'n/a')(s.split())
