save = []


def min_length_num(num_dig, ord_max):
    for i in range(ord_max):
        if i == len(save):
            save.append(len(str(sum((j + 1)**(i - j) for j in range(i)))))
        if save[i] == num_dig:
            return [True, i + 1]
    return [False, -1]
