def ranking(people):
    people = people[:]
    people.sort(key=lambda person: (-person['points'], person['name']))
    for (i, person) in enumerate(people):
        if i and person['points'] == people[i - 1]['points']:
            person['position'] = people[i - 1]['position']
        else:
            person['position'] = i + 1
    return people
