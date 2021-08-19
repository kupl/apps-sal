def positive_sum(arr):
    # Your code here
    pos_arr = list([x for x in arr if x > 0])
    if pos_arr:
        return sum(pos_arr)
    return 0
