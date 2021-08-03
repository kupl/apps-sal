def detect_operator(num):
    d = {'Golden Telecom': ['039'], 'MTS': ['050', '066', '095', '099'], 'Life:)': ['063', '093'],
         'Kyivstar': ['067', '096', '097', '098'], 'Beeline': ['068']}
    return next((k for k in d if num[1: 4] in d[k]), 'no info')
