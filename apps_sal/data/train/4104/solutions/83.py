def max_tri_sum(numbers):
    srt_lst = sorted(set(numbers))
    return sum(srt_lst[-3:])
