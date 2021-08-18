def order_weight(strng):
    weight_list = strng.split()
    faux_list = []
    for weight in weight_list:
        total = 0
        for number in weight.strip():
            total = total + int(number)
        faux_weight, real_weight = total, weight
        faux_list.append((faux_weight, real_weight))

    final_manipulated_list = []
    for x, y in sorted(faux_list):
        final_manipulated_list.append(y)
    return " ".join(final_manipulated_list)
