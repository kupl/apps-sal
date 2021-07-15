import functools as ft

def find_difference(a, b):
    return abs(ft.reduce((lambda x, y: x * y), a) - ft.reduce((lambda x, y: x * y), b))    
