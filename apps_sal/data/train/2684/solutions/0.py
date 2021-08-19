def ordering_beers(beers):
    assert 0 <= beers < 100
    units = ['', 'jeden', 'dwa', 'trzy', 'cztery', 'piec', 'szesc', 'siedem', 'osiem', 'dziewiec', 'dziesiec', 'jedenascie', 'dwanascie', 'trzynascie', 'czternascie', 'pietnascie', 'szesnascie', 'siedemnascie', 'osiemnascie', 'dziewietnascie']
    tens = ['', '', 'dwadziescia', 'trzydziesci', 'czterdziesci', 'piecdziesiat', 'szescdziesiat', 'siedemdziesiat', 'osiemdziesiat', 'dziewiecdziesiat']
    if beers == 0:
        order = 'Woda mineralna'
    elif beers == 1:
        order = 'Jedno piwo'
    elif beers < 20:
        order = units[beers] + ' piw'
    else:
        order = tens[beers // 10] + ' ' * bool(beers % 10) + units[beers % 10] + ' piw'
    if beers % 10 in [2, 3, 4] and beers not in [12, 13, 14]:
        order += 'a'
    return order.capitalize() + ' poprosze'
