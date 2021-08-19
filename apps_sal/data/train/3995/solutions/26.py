def first(age):
    min_age = str(int(age / 2 + 7))
    max_age = str(int((age - 7) * 2))
    return [min_age, max_age]


def second(age):
    min_age = str(int(age - 0.1 * age))
    max_age = str(int(age + 0.1 * age))
    return [min_age, max_age]


def dating_range(age):
    return ['-'.join(first(age)), '-'.join(second(age))][age <= 14]
