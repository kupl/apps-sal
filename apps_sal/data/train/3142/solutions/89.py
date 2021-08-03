def seven_ate9(str_):
    return "".join(k for i, k in enumerate(str_) if str_[i - 1: i + 2] != "797")
