def paul(x):
    dict = {'kata':5, 'Petes kata': 10, 'life': 0, 'eating': 1}
    res = sum(dict.get(i, 0) for i in x)
           
    return 'Super happy!' if res < 40 else 'Happy!' if res < 70 else  'Sad!' if res <100 else 'Miserable!'

