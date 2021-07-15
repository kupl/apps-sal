def actually_really_good(foods):   
    phrase="You know what's actually really good? "
    if len(foods)==0:return phrase+"Nothing!"
    elif len(foods)==1:return phrase+f"{foods[0].capitalize()} and more {foods[0].lower()}."
    else:return phrase+f"{foods[0].capitalize()} and {foods[1].lower()}."
