def series_sum(n):
    if n == 0:
        return '0.00'
    else:
        counter = 1
        list = [1]
        while counter < n:
            list.append(1 / (1 + 3 * counter))
            counter += 1
        flt = round(sum(list), 2)
        result = format(flt, '.2f')
        return result
