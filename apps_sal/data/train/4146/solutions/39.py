def is_sorted_and_how(arr):
    delta_value = []
    positive_num = 0
    negtive_num = 0
    for i in range(len(arr) - 1):
        delta_value.append(arr[i + 1] - arr[i])
    for i in range(len(delta_value)):
        if delta_value[i] >= 0:
            positive_num += 1
        else:
            negtive_num += 1
    if positive_num == len(delta_value):
        return 'yes, ascending'
    elif negtive_num == len(delta_value):
        return 'yes, descending'
    else:
        return 'no'
