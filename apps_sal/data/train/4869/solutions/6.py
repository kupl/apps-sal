def find_seventh_sons_of_seventh_sons(jstring):
    return set(has_7_of_7_son(json.loads(jstring)))


def has_7_of_7_son(person, parent_is_7=False):
    counter = 0
    result = []
    broken = False
    if person['children']:
        for child in person['children']:
            if child['gender'] == 'male':
                counter += 1
            else:
                broken = True
            if counter == 7 and not broken:
                if parent_is_7:
                    result.append(child['name'])
                result.extend(has_7_of_7_son(child, True))
            result.extend(has_7_of_7_son(child, False))
    return result
