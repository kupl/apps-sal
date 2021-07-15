def unpack(l):
    pac = []
    for e in l:
        if type(e) not in [tuple, list, set, dict]:
            pac.append(e)
        elif type(e) == dict:
            pac += unpack(list(e.items()))
        else:
            pac += unpack(e)
    return pac
