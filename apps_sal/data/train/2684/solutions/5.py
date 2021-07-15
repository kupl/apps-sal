singleNums = ["zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc" , "siedem", "osiem", "dziewiec"]
tenth = ["dziesiec", "jedenascie", "dwanascie", "trzynascie", "czternascie", "pietnascie", "szesnascie", "siedemnascie", "osiemnascie", "dziewietnascie"] 
tens = ["dziesiec", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat", "szescdziesiat", "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"]

def ordering_beers(beers):
    
    if beers < 0:
        raise ValueError('No negative values')
    elif beers < 1:
        return "Woda mineralna poprosze"
    elif beers == 1:
        return "Jedno piwo poprosze"
    
    
    whole = beers // 10
    modulo = beers % 10
    
    if beers > 10 and beers < 15:
        noun = 'piw'
    elif modulo > 1 and modulo < 5:
        noun = 'piwa'
    else:
        noun = 'piw'
    
    if beers < 10:
        numeral = singleNums[beers]
    elif beers > 9 and beers < 20:
        numeral = tenth[modulo]
    elif modulo == 0 and beers > 19:
        numeral = tens[whole-1]
    else:
        numeral = tens[whole-1] + ' ' + singleNums[modulo]
    
    return numeral.capitalize() + ' ' + noun + ' poprosze'
