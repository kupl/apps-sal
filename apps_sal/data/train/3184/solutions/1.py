def total_bill(s):
    num = s.count('r')
    return (num - num // 5) * 2
