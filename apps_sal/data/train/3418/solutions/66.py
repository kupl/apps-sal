def reverse_list(l):
    reversed_arr = []
    for i in range(len(l)):
        reversed_arr.append(l[len(l) - 1 - i])
    return reversed_arr
