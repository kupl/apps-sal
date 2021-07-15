from collections import Counter
def odd_ones_out(numbers):
    dct = Counter(numbers)
    return [num for num in numbers if dct[num]%2 == 0]

