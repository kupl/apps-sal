from inspect import getgeneratorstate as gg


def check_generator(gen):
    return {'GEN_CREATED': 'Created', 'GEN_SUSPENDED': 'Started', 'GEN_CLOSED': 'Finished'}[gg(gen)]
