def seven_ate9(str_):
    result = str_[0]

    for i in range(1, len(str_) - 1):
        if not (str_[i - 1] == "7" and str_[i] == "9" and str_[i + 1] == "7"):
            result += str_[i]

    result += str_[-1]

    return result
