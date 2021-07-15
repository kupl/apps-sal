def remove_smallest(numbers):
    return [x for i, x in enumerate(numbers) if i != min(range(len(numbers)), key=numbers.__getitem__)]
