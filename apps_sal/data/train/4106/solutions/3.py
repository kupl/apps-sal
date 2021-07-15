def self_converge(number):
    digits_num = len(str(number))
    count = 0
    prev = []
    while number not in prev:
        prev.append(number)
        digits = [c for c in str(number)]
        n_asc = int(''.join(sorted(digits, reverse=False)))
        n_desc = int(''.join(sorted(digits, reverse=True)))
        while len(str(n_desc))<digits_num:
            n_desc *=10
        number = n_desc-n_asc
        if number==0:
            return -1
        count += 1
    return count
