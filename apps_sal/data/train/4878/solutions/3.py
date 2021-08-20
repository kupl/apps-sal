from inspect import getgeneratorstate


def check_generator(gen):
    _ = getgeneratorstate(gen)
    if _ == 'GEN_CREATED':
        return 'Created'
    if _ == 'GEN_RUNNING' or _ == 'GEN_SUSPENDED':
        return 'Started'
    else:
        return 'Finished'
