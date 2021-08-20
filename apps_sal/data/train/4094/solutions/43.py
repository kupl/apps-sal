def count_positives_sum_negatives(arr):
    for a in arr:
        while True:
            amount = len([a for a in arr if a > 0])
            suma = sum((a for a in arr if a < 0))
            return [amount, suma]
    else:
        return []
