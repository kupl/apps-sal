def get_planet_name(id):
    return switch(id)


def switch(id):
    case = {'case1': {'name': 'Mercury'}, 'case2': {'name': 'Venus'}, 'case3': {'name': 'Earth'}, 'case4': {'name': 'Mars'}, 'case5': {'name': 'Jupiter'}, 'case6': {'name': 'Saturn'}, 'case7': {'name': 'Uranus'}, 'case8': {'name': 'Neptune'}}
    caseKey = 'case' + str(id)
    return case.get(caseKey, case.get('case1')).get('name')
