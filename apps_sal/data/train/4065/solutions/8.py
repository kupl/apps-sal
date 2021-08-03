def get_sequence(offset, size):
    num = max(offset, 1023456789)
    digits = set("0123456789")
    ret = []
    for _ in range(size):
        while num < 9876543210:
            if set(str(num)) == digits:
                ret.append(num)
                break
            else:
                num += 1
        num += 1

    return ret
