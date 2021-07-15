from itertools import combinations
def two_sum(numbers, target):
    for i1,i2 in  combinations(list(range(len(numbers))), 2):
        if numbers[i1] + numbers[i2] == target:
            return i1,i2


