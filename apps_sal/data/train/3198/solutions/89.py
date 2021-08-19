def check_exam(arr1, arr2):
    liste = []
    for (i, x) in enumerate(arr1):
        y = arr2[i]
        if x != y:
            if y == '':
                liste.append(0)
            else:
                liste.append(-1)
        else:
            liste.append(4)
    x = sum(liste)
    if x < 0:
        return 0
    else:
        return x
