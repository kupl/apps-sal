def count_inversions(collection):
    lenghts = len(collection)
    swapped = False
    swapped_counter = 0
    for i in range(lenghts - 1):
        for j in range(lenghts - i - 1):
            if collection[j] > collection[j + 1]:
                (collection[j], collection[j + 1]) = (collection[j + 1], collection[j])
                swapped = True
                swapped_counter += 1
        if not swapped:
            break
    return swapped_counter
