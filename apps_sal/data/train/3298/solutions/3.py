def avg_array(arrs):
    return [(sum(ar[i] for ar in arrs)) / len(arrs) for i in range(len(arrs[0]))]
