def dating_range(age):
    if age <= 14:
        mini = int(age - 0.1 * age)
        maxi = int(age + 0.1 * age)
    else:
        mini = age // 2 + 7
        maxi = (age - 7) * 2
    return '{}-{}'.format(mini, maxi)
