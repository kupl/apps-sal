from math import factorial as f
def strong_num(number):
    return ['Not Strong !!','STRONG!!!!'][number == sum(f(int(d)) for d in str(number))]
    
    

