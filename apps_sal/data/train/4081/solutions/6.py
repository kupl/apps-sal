# Which bump protrudes the farthest?
def first_tooth(array):
    if len(array) == 1:
        return 0
    else:
        max_diff = -1
        max_diff_indices = []
        i = 0
        while i < len(array):
            if i == 0:
                diff = array[i] - array[i + 1]
            elif i == len(array) - 1:
                diff = array[i] - array[i - 1]
            else:
                diff = array[i] - array[i - 1] + array[i] - array[i + 1]
            if diff > max_diff:
                max_diff = diff
                max_diff_indices = [i]
            elif diff == max_diff:
                max_diff_indices.append(i)
            i += 1
        if len(max_diff_indices) > 1:
            return -1
        else:
            return max_diff_indices[0]
