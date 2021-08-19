def check_generator(g):
    return {'GEN_CREATED': 'Created', 'GEN_CLOSED': 'Finished'}.get(__import__('inspect').getgeneratorstate(g), 'Started')
