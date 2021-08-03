def HQ9(code):
    def generate_lyrics():
        rv = '99 bottles of beer on the wall, 99 bottles of beer.'
        for i in range(98, -1, -1):
            plural = '' if i == 1 else 's'
            beers = 'no more' if i == 0 else str(i)
            rv += '\nTake one down and pass it around, {} bottle{} of beer on the wall.'.format(beers, plural)
            rv += '\n{} bottle{} of beer on the wall, {} bottle{} of beer.'.format(beers if beers.isnumeric() else beers.capitalize(), plural, beers, plural)
        else:
            rv += '\nGo to the store and buy some more, 99 bottles of beer on the wall.'
        return rv
    return {
        'H': 'Hello World!',
        'Q': code,
        '9': generate_lyrics()
    }.get(code, None)
