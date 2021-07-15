from collections import defaultdict

def delete_nth(order,max_e):
    count = defaultdict(int)
    ret = []
    for x in order:
        count[x] += 1
        if count[x] <= max_e:
            ret.append(x)
    return ret
