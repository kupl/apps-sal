import inspect


def check_generator(gen):
    state = inspect.getgeneratorstate(gen)
    return [['Created', 'Started'][state == 'GEN_SUSPENDED'], 'Finished'][state == 'GEN_CLOSED']
