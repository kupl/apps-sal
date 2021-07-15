def any_odd(x):
    return '1' in f'0{x:b}'[-2::-2]
