def count_positives_sum_negatives(arr): return [len([e for e in arr if e > 0]), sum(e for e in arr if e < 0)] if arr else []
