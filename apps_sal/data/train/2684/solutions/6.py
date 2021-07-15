ones = ["jeden", "dwa", "trzy", "cztery", "piec", "szesc" , "siedem", "osiem", "dziewiec"]
teens = ["dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie", "pietnascie", "szesnascie", "siedemnascie", "osiemnascie", "dziewietnascie"]
tens = ["dziesiec", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat", "szescdziesiat", "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"]

def ordering_beers(beers):
    if beers < 0: raise 'No negative beers'
    if not beers: return 'Woda mineralna poprosze'
    output = ''
    ending = 'o' if beers == 1 else 'a' if (beers % 10) in (2, 3, 4) and not beers in (12, 13, 14) else ''
    if beers > 19:
        output = tens[beers // 10 - 1]
        beers %= 10
    elif beers > 9:
        output = teens[beers - 10]
        beers = 0
    if beers:
        if output: output += ' '
        output += 'jedno' if beers == 1 and not ' ' in output else ones[beers - 1]
    return f'{output} piw{ending} poprosze'.capitalize()
