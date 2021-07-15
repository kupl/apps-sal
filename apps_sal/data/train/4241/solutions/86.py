def sequence_sum(begin_number, end_number, step):
    ans = [i * step + begin_number for i in range((end_number - begin_number) // step + 1)]
    return sum(ans)
