def count_positives_sum_negatives(arr):
    sum = 0
    count = 0
    tableau = 2 * [0]
    if arr == []:
        return []
    else:
        for loop in range(len(arr)):
            if arr[loop] > 0:
                sum = sum + 1
            else:
                count = count + arr[loop]
            tableau = [sum, count]

        return tableau
