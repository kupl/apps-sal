from math import ceil
def find_ball(scales, n):
    li = list(range(n))
    while len(li)!=1:
        d = ceil(len(li) / 3)
        who = scales.get_weight(li[:d], li[-d:])
        li = [li[d:-d], li[-d:], li[:d]][who]
    return li[0] 
