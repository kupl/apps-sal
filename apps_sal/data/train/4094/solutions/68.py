def count_positives_sum_negatives(arr):
    kol_polozh = 0
    summ_otric = 0
    a = []
    if arr == []:
        return []
    else:
        for i in range(0, len(arr), 1):
            if arr[i] > 0:
                kol_polozh = kol_polozh + 1
            if arr[i] < 0:
                summ_otric = summ_otric + arr[i]
            a = [kol_polozh, summ_otric]

    return a
