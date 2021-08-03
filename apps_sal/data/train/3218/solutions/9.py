from operator import itemgetter


def SJF(jobs, index):
    total = 0
    for i, duration in sorted(enumerate(jobs), key=itemgetter(1)):
        total += duration
        if i == index:
            return total
