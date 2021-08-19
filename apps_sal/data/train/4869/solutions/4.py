import json


def validate_sons(data):
    if data['gender'] == 'male' and len(data['children']) >= 7:
        if all([x['gender'] == 'male' for x in data['children'][:7]]):
            if len(data['children'][6]['children']) >= 7:
                if all([x['gender'] == 'male' for x in data['children'][6]['children'][:7]]):
                    return True
    return False


def find_seventh_sons_of_seventh_sons(jstring):
    data = json.loads(jstring)
    result = []
    stack = [data]
    while len(stack) != 0:
        a = stack.pop()
        for children in a['children']:
            stack.append(children)
        if validate_sons(a):
            result.append(a['children'][6]['children'][6]['name'])
    return set(result)
