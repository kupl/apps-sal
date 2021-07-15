def remove_smallest(numbers):
    if len(numbers)<1:
        return numbers
    else:
        return numbers[:numbers.index(min(numbers))]+numbers[numbers.index(min(numbers))+1:]
