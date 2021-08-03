def balanced_num(number):
    if number < 100:
        return 'Balanced'
    array = [int(x) for x in str(number)]
    length = len(array)
    balmiddle = length // 2 - 1 if length % 2 == 0 else length // 2
    leftsum = 0
    rightsum = 0
    for x in range(balmiddle):
        leftsum += array[x]
        rightsum += array[len(array) - x - 1]
    return 'Balanced' if leftsum == rightsum else 'Not Balanced'
