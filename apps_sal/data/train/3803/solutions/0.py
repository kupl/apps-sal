from collections import defaultdict


def update_inventory(cur_stock, new_stock):
    answer = defaultdict(int)
    for stock, item in cur_stock + new_stock:
        answer[item] += stock
    return [(answer[item], item) for item in sorted(answer)]
