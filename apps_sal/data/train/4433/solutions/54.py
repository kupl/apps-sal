from operator import __and__, __or__, __xor__ 

operators = {
    'AND': __and__,
    'OR': __or__,
    'XOR': __xor__
}

def logical_calc(arr, op):
    acc = arr[0]
    
    for item in arr[1:]:
        acc = operators[op](acc, item)
        
    return acc
