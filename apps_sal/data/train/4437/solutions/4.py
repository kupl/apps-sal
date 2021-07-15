CULPRITS = {
    str: 'Zach',
    int: 'Monica', float: 'Monica'
}

def cookie(x):
    return "Who ate the last cookie? It was {}!".format(CULPRITS.get(type(x), 'the dog'))
