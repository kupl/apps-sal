def automorphic(n):
    result = {True: 'Automorphic', False: 'Not!!'}
    square = str(n ** 2)
    number = str(n)
    return result[number == square[-len(number):]]
