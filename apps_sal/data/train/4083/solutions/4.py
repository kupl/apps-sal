def performant_smallest(lst, n):
    c = [0] * 201  # Our counter.
    for itm in lst:
        c[itm + 100] += 1  # Map each number to num+100.
    res, sm = [0] * n, 0
    for k in range(201):  # Iterate through the numbers in our counter.
        sm += c[k]
        if sm >= n:
            c[k] += n - sm  # The sum of `c[:k+1]` should be equal to `n`, and this would give us the count of the `n` smallest elements.
            break
    sm = 0
    for itm in lst:  # Iterate through the list to present the elements in their appearance order in the list.
        v = itm + 100  # The mapping between the list item and its index in our counter.
        if v <= k and c[v] > 0:  # The item is one of the `n` smallest items.
            res[sm] = itm  # Place it in its position in the result list.
            sm += 1
            c[v] -= 1
        if sm == n:
            break
    return res
