def calc_fuel(n):
    result = {}
    wholeTime = n * 11
    result['lava'] = wholeTime // 800
    wholeTime -= 800 * result['lava']
    result['blaze rod'] = wholeTime // 120
    wholeTime -= 120 * result['blaze rod']
    result['coal'] = wholeTime // 80
    wholeTime -= 80 * result['coal']
    result['wood'] = wholeTime // 15
    wholeTime -= 15 * result['wood']
    result['stick'] = wholeTime // 1
    return result
