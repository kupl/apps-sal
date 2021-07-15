def even(n):
    return n % 2 == 0

def split_all_even_numbers(numbers, way):
    lst = []
    for n in numbers:
        if even(n): lst += split(n, way)
        else: lst += [n]
    return lst                
        
def split(num, way):  
    if way == 0:
        half = num / 2
        return [half-1, half+1] if even(half) else [half, half]
    elif way == 1:
        return [1, num - 1]
    elif way == 2:
        return next([d] * (num // d) for d in range(num-1, 0, -2) if num % d == 0)
    elif way == 3:
        return [1] * num
