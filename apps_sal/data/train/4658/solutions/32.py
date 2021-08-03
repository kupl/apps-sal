
def max_product(lst, n_largest_elements):
    sort_lst = sorted(lst)
    output = 1
    for i in range(1, n_largest_elements + 1):
        output = output * sort_lst[-i]
    return output
