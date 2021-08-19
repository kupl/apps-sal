from math import floor


def dating_range(age):
    if age <= 14:
        mini = [str(floor(age - 0.1 * age))]
        maxi = [str(floor(age + 0.1 * age))]
        return '-'.join(mini + maxi)
    else:
        mini = [str(floor(age / 2 + 7))]
        maxi = [str(floor((age - 7) * 2))]
        return '-'.join(mini + maxi)
