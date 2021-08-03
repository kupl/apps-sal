names = {
    str: 'Zach',
    float: 'Monica',
    int: 'Monica',
}


def cookie(x):
    return f"Who ate the last cookie? It was {names.get(type(x),'the dog')}!"
