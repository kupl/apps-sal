def find_needed_guards(k):
    return sum(len(i) // 2 for i in ''.join([('0', '1')[i] for i in k]).split('1'))
