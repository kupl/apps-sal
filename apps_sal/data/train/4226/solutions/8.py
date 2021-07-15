def remove_smallest(numbers):
    #    raise NotImplementedError("TODO: remove_smallest")
    return [numbers[i] for i in range(len(numbers)) if i != numbers.index(min(numbers))]
