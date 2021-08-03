def seven_ate9(str_):
    lst = []
    x = 0
    while len(str_) > x:
        if str_[x] == "9" and len(str_) > x + 1:
            if str_[(x - 1)] == "7" and str_[(x + 1)] == "7":
                x = x + 1
            else:
                lst.append(str_[x])
                x = x + 1
        else:
            lst.append(str_[x])
            x = x + 1
    return str("".join(lst))
