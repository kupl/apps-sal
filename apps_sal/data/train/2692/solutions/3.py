def bubble(lst):
    result = []
    mod = lst.copy()
    swap = True
    while swap:
        swap = False
        for i in range(len(mod) - 1):
            if mod[i] > mod[i + 1]:
                (mod[i], mod[i + 1]) = (mod[i + 1], mod[i])
                swap = True
                result.append(mod.copy())
    return result
