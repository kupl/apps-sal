import json


def find_seventh_sons_of_seventh_sons(jstring):
    return seek4SeventhJSon(json.loads(jstring))


def seek4SeventhJSon(parent, _7up=False):
    (nSons, _7sons7) = (0, set())
    for (n, child) in enumerate(parent['children'], 1):
        if child['gender'] == 'male':
            nSons += 1
            _7sons7 |= seek4SeventhJSon(child, n == nSons == 7)
            if n == nSons == 7 and _7up:
                _7sons7.add(child['name'])
    return _7sons7
