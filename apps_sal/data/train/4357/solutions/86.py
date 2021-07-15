def nth_smallest(arr, pos):
    l = len(arr)
    liste = arr
    n = 1
    while n != pos:
        liste.remove(min(liste))
        n = n + 1
    return min(liste)
