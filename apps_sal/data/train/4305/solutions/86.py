def order_weight(strng):
    numbers = [int(i) for i in strng.split()]

    weights = []
    for number in numbers:
        weight = sum(map(int, str(number)))
        mylst = [number, weight]
        weights.append(mylst)
    
    res_list = []
    for lst in sorted(weights, key=lambda x: (x[1], str(x[0]))):
        res_list.append(str(lst[0]))
    
    return " ".join(res_list)

