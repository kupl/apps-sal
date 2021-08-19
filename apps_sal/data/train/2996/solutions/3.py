def how_much_coffee(events):
    coffee = sum((1 + e.isupper() for e in events if e.lower() in ('cw', 'cat', 'dog', 'movie')))
    return coffee if coffee <= 3 else 'You need extra sleep'
