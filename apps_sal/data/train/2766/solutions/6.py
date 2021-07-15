def check_concatenated_sum(num, n):
    num = abs(num)
    return sum(int(i*n) for i in str(num) if n)==num
