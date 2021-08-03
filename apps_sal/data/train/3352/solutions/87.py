def find_longest(arr):
    # your code here
    res = 0
    answer = 0
    for el in arr:
        max_len = len(str(el))
        if res < max_len:
            res = max_len
            answer = el
    return answer
