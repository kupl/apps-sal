def parse_float(st):
    for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if i in st or type(st) == list:
            return None
        else:
            return float(st)
