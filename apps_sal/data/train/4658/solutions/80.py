def max_product(lst, n_largest_elements):
    answer = 1
    lst.sort(reverse = True)
    for x in range(n_largest_elements):
        answer *= lst[x]
    return answer
