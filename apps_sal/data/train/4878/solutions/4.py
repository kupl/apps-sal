from inspect import getgeneratorstate


def check_generator(g):
    return {'R': 'Created', 'U': 'Started', 'L': 'Finished'}[getgeneratorstate(g)[5]]
