from collections import OrderedDict


def mutate_my_strings(s1, s2):
    return '\n'.join(OrderedDict.fromkeys((s2[:i] + s1[i:] for i in range(len(s1) + 1)))) + '\n'
