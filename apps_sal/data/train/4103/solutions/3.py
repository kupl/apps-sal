def naughty_or_nice(d): return max(['Nice', 'Naughty'], key=[x for y in d.values() for x in y.values()].count) + '!'
