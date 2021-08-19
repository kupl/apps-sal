def is_divide_by(number, a, b):
    div = float(0)
    div2 = float(0)

    div = number / a
    div2 = number / b

    div3 = number // a
    div4 = number // b
    if div == div3 and div2 == div4:
        return True  # good luck
    else:
        return False
