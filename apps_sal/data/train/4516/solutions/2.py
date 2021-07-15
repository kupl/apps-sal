def multiple(x):
    val = ''
    if x % 3 == 0:
        val += 'Bang'
    if x % 5 == 0:
        val += 'Boom'
    if val == '':
        val = 'Miss'
    return val
