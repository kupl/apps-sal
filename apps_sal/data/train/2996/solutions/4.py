def how_much_coffee(events):
    return (lambda coffee: coffee if coffee < 4 else 'You need extra sleep')(sum(map(lambda x: 2 if x.isupper() else 1, filter(lambda x: __import__('re').match('(?i)^(cw|dog|cat|movie)$', x), events))))
