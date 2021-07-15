def tail_swap(strings):
    return '{0}:{3} {2}:{1}'.format(*[j for i in strings for j in i.split(':')]).split()
