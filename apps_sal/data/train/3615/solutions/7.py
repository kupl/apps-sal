from copy import deepcopy


def presentation_agenda(presentation_agenda):
    data = deepcopy(presentation_agenda)
    for person in data:

        B = []
        for p in presentation_agenda:
            if p['person'] != person['person']:
                B += p['dest']
        person['dest'] = sorted(list(set(person['dest']) - set(B)))

    return [person for person in data if person['dest']]
