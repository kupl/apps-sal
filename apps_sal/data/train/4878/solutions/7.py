from inspect import getgeneratorstate

def check_generator(gen):
    state = getgeneratorstate(gen)
    if state == 'GEN_CREATED': return 'Created'
    elif state == 'GEN_SUSPENDED': return 'Started'
    else: return 'Finished'
