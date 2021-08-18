def arr(n=0):
    num_list = []

    if n < 1:
        return num_list
    else:
        for i in range(n):
            if i < n:
                num_list.append(i)
        return num_list
