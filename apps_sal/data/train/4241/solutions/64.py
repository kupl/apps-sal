def sequence_sum(begin_number, end_number, step):
    sum = 0
    st = step
    for i in range(begin_number, end_number + 1):
        if st == step:
            sum += i
            st = 0
        st += 1
    return sum
