def solve(arr):
    positive_set = set()
    negative_set = set()
    for num in arr:
        if num > 0:
            positive_set.add(num)
        else:
            negative_set.add(-num)
    number = positive_set.symmetric_difference(negative_set)
    popped_number = number.pop()
    return popped_number if popped_number in arr else -popped_number
