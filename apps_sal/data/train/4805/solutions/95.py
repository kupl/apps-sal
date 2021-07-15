def check(seq, elem):
    total = 0
    print(len(seq))
    for i in seq:
        if i == elem:
            return True
        else:
            total += 1
            if total == len(seq):
                return False
