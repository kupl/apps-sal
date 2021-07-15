def check_concatenated_sum(num, l):
    return sum([int(x*l) for x in str(abs(num))]) == abs(num) if l>0 else False
