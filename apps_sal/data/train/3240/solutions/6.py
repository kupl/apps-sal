def true_binary(n):
    temp = bin(n)[2:]
    return [1 if i == "1" else -1 for i in temp[-1] + temp[:-1]]
