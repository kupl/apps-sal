def find77(j, son=False, sons=[]):
    sc = 0
    for c in j['children']:
        if c['gender'] == 'male':
            sc += 1
        else:
            sc = 8
        if sc == 7 and 'children' in list(c.keys()):
            sons = find77(c, True, sons)
        elif 'children' in list(c.keys()):
            sons = find77(c, False, sons)
        if sc == 7 and son:
            sons = [c['name']] + sons

    return sons


def find_seventh_sons_of_seventh_sons(jstring):
    jstring = eval(jstring)
    sonlist = find77(jstring, False)
    if len(sonlist) == 0:
        return set()
    else:
        return eval(str(sonlist).replace("[", "{").replace("]", "}"))
