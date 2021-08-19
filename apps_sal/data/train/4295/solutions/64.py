def balanced_num(number):
    lstofnum = [int(num) for num in str(number)]
    (left, right) = (0, 0)
    while len(lstofnum) > 2:
        left += lstofnum.pop(0)
        right += lstofnum.pop(-1)
    return 'Balanced' if left == right else 'Not Balanced'
