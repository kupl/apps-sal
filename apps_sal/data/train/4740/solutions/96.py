def row_sum_odd_numbers(n):
    data = {1: {'last': 1, 'sum': 1}}
    while max(data.keys()) <= n:
        id_max = max(data.keys())
        last, summ = data[id_max]['last'], data[id_max]['sum']
        a = [i for i in range(last + 2, id_max * 2 + last + 4, 2)]
        id_max += 1
        data[id_max] = {'last': a[-1], 'sum': sum(a)}
    return data[n]['sum']
