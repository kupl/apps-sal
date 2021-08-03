import functools
import operator


def order_weight(strng):
    # your code
    if strng == "":
        return ""
    else:
        x = strng.split(" ")
        y = []
        weighted_weights = dict()
        for item in range(len(x)):
            actualweight = x[item]
            y.append(functools.reduce(operator.add, [int(actualweight[i]) for i in range(len(actualweight))]))
            weighted_weights[x[item]] = y[item]
        x = sorted(x)
        listofweights = sorted(x, key=weighted_weights.get)
        return ' '.join(listofweights)
