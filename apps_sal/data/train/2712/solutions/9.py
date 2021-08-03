def loneliest(number):
    if (str(number)).count("1") == 0:
        return False
    if (str(number)).count("1") == len(str(number)):
        return True

    number = [int(a) for a in str(number)]
    score = []
    one = []
    for idx, nr in enumerate(number):

        b = idx - nr
        f = idx + nr + 1
        s = 0

        if b < 0:
            b = 0
        if f > len(number):
            f = len(number)

        s += sum(number[b:idx])
        s += sum(number[idx + 1:f])

        if nr == 1:
            one.append(s)
        else:
            score.append(s)

    score.sort()
    one.sort()
    if score[0] >= one[0]:
        return True
    return False
