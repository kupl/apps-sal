def min_sum(arr):
    answer = 0
    for i in range(int(len(arr) / 2)):
        Max = max(arr)
        Min = min(arr)

        arr.remove(Max)
        arr.remove(Min)
        answer += Min * Max
    return(answer)
