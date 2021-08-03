def alex_mistakes(number_of_katas, time_limit):
    left = (time_limit - 6 * number_of_katas) // 5
    bits = left.bit_length()
    if left + 1 == 1 << bits:
        return bits
    return bits - 1
