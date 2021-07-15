def new_numeral_system(number):
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n = chars.index(number)
    return [f'{chars[i]} + {chars[n-i]}' for i in range(0, n//2+1)]

