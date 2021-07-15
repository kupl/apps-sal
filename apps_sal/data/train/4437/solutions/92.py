def cookie(x):
    output = 'Zach' if type(x)==str else 'Monica' if type(x)==int or type (x)==float else 'the dog'
    return "Who ate the last cookie? It was {}!".format(output)
