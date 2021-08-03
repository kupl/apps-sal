c = [[1]]
p = [1, 1]
c.append(p)
for i in range(1, 2100):
    a = [1]
    for j in range(1, i + 1):
        a.append(p[j - 1] + p[j])
    a.append(1)
    c.append(a)
    p = a


def roll_dice(rolls, sides, threshold):
    if threshold <= rolls:
        return 1
    if threshold > rolls * sides:
        return 0
    threshold -= rolls + 1
    sum_ = 0.0
    i = 0
    while (threshold >= 0):
        sum_ += (-1)**i * c[rolls][i] * c[threshold + rolls][threshold]
        threshold -= sides
        i += 1
    return 1.0 - sum_ / (sides ** rolls)
