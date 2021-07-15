def check_concatenated_sum(number, k):
    return sum(int(d * k) for d in str(abs(number))) == abs(number) if k else False

