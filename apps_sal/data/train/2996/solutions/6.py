def how_much_coffee(events):
    coffees = 0
    for s in ['cw', 'cat', 'dog', 'movie']:
        coffees += events.count(s)
        coffees += 2* events.count(s.upper())
    if coffees > 3:
        return 'You need extra sleep'
    return coffees

