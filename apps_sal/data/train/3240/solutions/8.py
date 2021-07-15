def true_binary(n):
    suma = "{:0b}".format(n)
    ans = [int(suma[0])]
    for i in range(1,len(suma)):
        if suma[i-1] == "0": ans.append(-1)
        else: ans.append(1)
    return ans
