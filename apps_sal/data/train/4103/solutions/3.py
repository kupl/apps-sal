naughty_or_nice = lambda d:max(['Nice', 'Naughty'], key=[x for y in d.values() for x in y.values()].count) + '!'
