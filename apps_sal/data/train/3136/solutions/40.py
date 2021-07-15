drink_pairs = {'kid':'toddy','teen':'coke','youngAdult':'beer','adult':'whisky'}

def people_with_age_drink(age):
    if age >= 21:
        return 'drink ' + drink_pairs['adult']
    elif age < 21 and age >= 18:
        return 'drink ' + drink_pairs['youngAdult']
    elif age < 18 and age >= 14:
        return 'drink ' + drink_pairs['teen']
    else:
        return 'drink ' + drink_pairs['kid']
