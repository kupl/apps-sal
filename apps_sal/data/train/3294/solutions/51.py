def converter(mpg):
    result = '{:.2f}'.format(mpg * 1.609344 / 4.54609188)
    return float(result) if result[-1] != '0' else float(result[:-1])
