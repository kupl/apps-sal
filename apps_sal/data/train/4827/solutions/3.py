from __future__ import division
import numpy as np


def stats_disc_distr(distrib):
    print(distrib)
    values = [i[0] for i in distrib]
    probs = [i[1] for i in distrib]

    if any(type(i) != int for i in values) and float(sum(probs)) != 1.0:
        return "It's not a valid distribution and furthermore, one or more variable value are not integers"
    elif sum(probs) > 1.0 + 1e-5 or sum(probs) < 1.0 - 1e-5:
        print(sum(probs))
        return "It's not a valid distribution"
    elif any(type(i) != int for i in values):
        return "All the variable values should be integers"

    mean = np.mean(values)
    var = sum([(values[i] - mean)**2 * probs[i] for i in range(len(values))])
    std_dev = var**0.5

    return [mean, var, std_dev]
