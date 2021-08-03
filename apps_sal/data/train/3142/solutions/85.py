def seven_ate9(str_):
    return str_[0] + "".join([c for i, c in enumerate(str_[1:-1], 1) if not ((c == "9") and (str_[i - 1] == str_[i + 1] == "7"))]) + str_[-1]
