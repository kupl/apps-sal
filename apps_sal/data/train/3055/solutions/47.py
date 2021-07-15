def sum_str(*str_nums):
    return str(sum(bool(n) and int(n) for n in str_nums))
