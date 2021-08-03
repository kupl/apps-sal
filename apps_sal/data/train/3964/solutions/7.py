def rank_of_element(arr, i):
    # your code here
    rank = 0
    for j in range(len(arr)):
        if j < i:
            if arr[j] <= arr[i]:
                rank += 1
        elif j > i:
            if arr[j] < arr[i]:
                rank += 1
    return rank
