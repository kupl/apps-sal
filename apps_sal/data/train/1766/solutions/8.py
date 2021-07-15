def skrzat(base, number):
    def to_binary(number):
        schroeppel2 = 0xAAAAAAAA
        return "From decimal: {} is {}".format(number, bin((int(number) + schroeppel2) ^ schroeppel2)[2:])
    def to_decimal(number):
        return "From binary: {} is {}".format(number, sum(int(d)*(-2)**i for i, d in enumerate(reversed(number))))

    if base == "b":
        return to_decimal(number)
    return to_binary(number)
