def multiples(m, n):
    i = 1
    final_list = []
    while i <= m:
        final_list.append(n*i)
        i += 1
    return final_list
