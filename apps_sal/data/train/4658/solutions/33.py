def max_product(lst, n_largest_elements):
    answer = 1
    lst = sorted(lst)
    for i in lst[-n_largest_elements:]:
        answer *= i
    return answer
