def sum_of_regular_numbers(arr):
    sum_ = 0
    i = 0
    while i < len(arr) - 1:
        seq = [arr[i], arr[i+1]]
        step = arr[i] - arr[i+1]
        j = i + 1
        while j < len(arr) - 1:
            if arr[j] - arr[j+1] != step:
                break
            seq.append(arr[j+1])
            j += 1
        if len(seq) >= 3:
            sum_ += sum(seq)
        i = j
    return sum_
