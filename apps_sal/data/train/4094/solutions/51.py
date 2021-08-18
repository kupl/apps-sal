def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    else:
        CountPos = 0
        SumNeg = 0
        for Index in range(len(arr)):
            if arr[Index] > 0:
                CountPos = CountPos + 1
            else:
                if arr[Index] < 0:
                    SumNeg = SumNeg + arr[Index]
        return [CountPos, SumNeg]
