def well(x):
    alfa = ('Fail!', 'Publish!', 'Publish!', 'I smell a series!')
    return alfa[min(3, max(x.count('good'), 0))]
