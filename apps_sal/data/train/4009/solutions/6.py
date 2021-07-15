from math import ceil


def digits_average(input):
    def return_average(a, b):
        return str(ceil((int(a) + int(b)) / 2))

    string_ = str(input)

    while len(string_) > 1:
        string_ = ''.join(
            return_average(a, b) for a, b in zip(string_, string_[1:]))

    return int(string_)
