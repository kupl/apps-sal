from inspect import getgeneratorstate as gt
d = {'GEN_CREATED':'Created', 'GEN_SUSPENDED':'Started'}
def check_generator(gen):
    return d.get(gt(gen), 'Finished')

