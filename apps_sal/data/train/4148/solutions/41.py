def sum_digits(number):
    splits = list(str(number))
    num_lst = []
    for num in splits:
        try:
            if type(int(num)) == int:
                num_lst.append(int(num))
        except:
            continue
    return sum(num_lst)
