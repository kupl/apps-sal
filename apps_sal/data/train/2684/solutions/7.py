def ordering_beers(beers):
    oneToTwenty = ['zero','jeden','dwa','trzy','cztery','piec','szesc','siedem','osiem',
        'dziewiec','dziesiec','jedenascie','dwanascie','trzynascie','czternascie',
        'pietnascie','szesnascie','siedemnascie','osiemnascie','dziewietnasce','dwadziescia']
    tens = ["dziesiec", "dwadziescia", "trzydziesci", "czterdziesci", "piecdziesiat", "szescdziesiat", 
        "siedemdziesiat", "osiemdziesiat", "dziewiecdziesiat"]
        
    if beers < 0:
        raise Exception("Only positive numbers!")
    elif beers == 0:
        return "Woda mineralna poprosze"
    elif beers == 1:
        return "Jedno piwo poprosze"
    elif beers <= 20:
        order = oneToTwenty[beers]
        order = order[:1].upper() + order[1:]
    else:
        order = tens[int(beers/10)-1] + " " + oneToTwenty[beers%10]
        order = order[:1].upper() + order[1:]
        
    if beers in [12,13,14]:
        order = order + " piw"
    elif beers%10 in [2,3,4]:
        order = order + " piwa"
    else:
        order = order + " piw"
        
    return order + " poprosze"
