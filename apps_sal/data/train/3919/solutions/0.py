def shuffled_array(s):
    result = sorted(s)
    result.remove(sum(result) // 2)
    return result
