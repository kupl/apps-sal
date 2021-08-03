import operator
from functools import reduce


def order_weight(strng):
    ans = []
    d = {}
    members = strng.split()
    for weight in members:
        sum_weight = 0
        for digit in weight:
            sum_weight += int(digit)
        if d.get(sum_weight) != None:
            d[sum_weight].append(weight)
        else:
            d[sum_weight] = [weight]
    li = sorted(list(d.items()), key=lambda el: el[0])
    for pair in li:
        if len(pair[1]) > 1:
            for mean in sorted(pair[1]):
                ans.append(str(mean))
        else:
            ans.append(str(pair[1][0]))
    return ' '.join(ans)
