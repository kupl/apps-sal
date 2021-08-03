import json


def f(data, level):
    if level == 0:
        yield data['name']
        return
    children = data['children']
    if len(children) >= 7 and all(child['gender'] == 'male' for child in children[:7]):
        yield from f(children[6], level - 1)
    for child in children:
        yield from f(child, 2)


def find_seventh_sons_of_seventh_sons(jstring):
    data = json.loads(jstring)
    return set(f(data, 2))
