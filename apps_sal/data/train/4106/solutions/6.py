def self_converge(number):

    def sub_converge(n, l, min_length):
        digits = [d for d in str(n)]
        while len(digits) < min_length:
            digits.append('0')
        asc = sorted(digits)
        desc = asc[::-1]
        if asc == desc:
            return -1
        next = int(''.join(desc)) - int(''.join(asc))
        if next in l:
            return len(l) + 1
        else:
            return sub_converge(next, l + [next], min_length)
    return sub_converge(number, [], len(str(number)))
