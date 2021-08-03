def how_much_coffee(events):
    res = 0
    for m in events:
        if m in ['cw', 'cat', 'dog', 'movie']:
            res += 1
        elif m in ['CW', 'DOG', 'MOVIE', 'CAT']:
            res += 2
    return (res if res < 4 else 'You need extra sleep')
