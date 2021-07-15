ORDER = {v:i for i,v in enumerate([':D', ':)', ':|', ':(', 'T_T'])}

def sort_emotions(arr, order):
    return sorted(arr, key=ORDER.__getitem__, reverse=not order)
