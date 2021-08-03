def bubblesort_once(L):
    if len(L) <= 1:
        return L
    if L[0] <= L[1]:
        return [L[0]] + bubblesort_once(L[1:])
    return [L[1]] + bubblesort_once([L[0]] + L[2:])
