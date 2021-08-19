import itertools


def rearranger(k, *args):
    (arrengment, prep) = (list(set(itertools.permutations([x for x in args]))), [])
    for (key, char) in enumerate(arrengment):
        seriesOfNumbers = [str(x) for x in arrengment[key]]
        number = int(''.join([x for x in ''.join(str(arrengment[key])) if x.isdigit()]))
        if number % k == 0:
            prep.append([seriesOfNumbers, number])
    try:
        minimum = min([x[1] for x in prep])
        answer = [x[0] for x in prep if x[1] == minimum] + [x[1] for x in prep if x[1] == minimum]
        if len(answer) == 0:
            return 'There is no possible rearrangement'
        elif len(answer) == 2:
            return 'Rearrangement: %s generates: %d divisible by %d' % (', '.join([x for x in answer[0]]), [y for (x, y) in enumerate(answer) if x % 2 != 0][0], k)
        elif len(answer) > 2:
            return 'Rearrangements: %s and %s generates: %d divisible by %d' % (', '.join([x for x in answer[0]]), ', '.join([x for x in answer[1]]), [y for (x, y) in enumerate(answer)][2], k)
    except ValueError:
        return 'There is no possible rearrangement'
