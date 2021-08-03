def count_positives_sum_negatives(arr):
    positive = 0
    negative = 0
    ans = []
    if not arr:
        return ans
    else:
        for i in range(len(arr)):
            if arr[i] > 0:
                positive = positive + 1
                print("positive: ", positive)
            else:
                negative = negative + arr[i]
                print("negative: ", negative)

        ans = [positive, negative]

        return ans
