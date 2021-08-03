def cookie(x):
    a = {str: 'Zach', int: 'Monica', float: 'Monica'}
    if type(x) in a.keys():
        return f"Who ate the last cookie? It was {a[type(x)]}!"
    else:
        return "Who ate the last cookie? It was the dog!"
