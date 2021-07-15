import json

def find_seventh_sons_of_seventh_sons(jstring):
    result, stack = set(), [json.loads(jstring)]
    while stack:
        person = stack.pop()
        if (len(person['children']) >= 7 and 
            all(child['gender'] == 'male' for child in person['children'][:7]) and
            len(person['children'][6]['children']) >= 7 and
            all(child['gender'] == 'male' for child in person['children'][6]['children'][:7])):
            result.add(person['children'][6]['children'][6]['name'])
        stack.extend(person['children'])
    return result
