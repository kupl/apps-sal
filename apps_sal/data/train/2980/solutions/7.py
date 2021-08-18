def check(n):
    set1 = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            set1.add(i)
            set1.add(n // i)
    return set1


def find_min_num(num_div):
    i = 1
    while 1:
        if len(check(i)) == num_div:
            return i
        i += 1
    return n
