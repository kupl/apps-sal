def detect_operator(num):
    operators = {'039': 'Golden Telecom', '050': 'MTS', '063': 'Life:)', '066': 'MTS', '067': 'Kyivstar', '068': 'Beeline', '093': 'Life:)', '095': 'MTS', '096': 'Kyivstar', '097': 'Kyivstar', '098': 'Kyivstar', '099': 'MTS'}
    return operators.get(str(num)[1:4], 'no info')
