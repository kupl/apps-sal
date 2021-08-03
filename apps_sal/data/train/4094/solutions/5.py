def count_positives_sum_negatives(input):
    if not input:
        return []
    count_ = 0
    sum_ = 0
    for element in input:
        if element > 0:
            count_ += 1
        elif element < 0:
            sum_ += element
    return [count_, sum_]
