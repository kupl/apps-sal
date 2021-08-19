def check_exam(arr1, arr2):
    liste = []
    for i, x in enumerate(arr1):  # weil sich enumerate immer auf Position und WErt (i, x) bezieht
        y = arr2[i]
        if ((x) != (y)):
            if y == (""):
                liste.append(0)
            else:
                liste.append(-1)
        else:
            liste.append(4)
    # return(x)

    x = sum(liste)
    if x < 0:
        return(0)
    else:
        return(x)
