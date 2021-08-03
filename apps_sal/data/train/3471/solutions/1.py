def mod256_without_mod(number):
    return number - number // 256 * 256
