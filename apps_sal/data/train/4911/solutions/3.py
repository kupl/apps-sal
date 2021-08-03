def sum_arrays(arr, shift):
    red = [[], arr][not shift]
    if shift > 0:
        la = len(arr)
        l0 = len(arr[0])
        lr = l0 + (shift * (la - (1)))
        ret = [0 * l0] * lr
        for i, x in zip(list(range(0, lr, shift)), list(range(la))):
            temp = ret[::]
            temp[i:l0 + i] = arr[x]
            red.append(temp)
    return [sum(a) for a in zip(*red)]
