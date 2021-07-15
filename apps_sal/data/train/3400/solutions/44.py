def even_numbers(arr,n):
    numberlist = []
    for eachnumber in arr[::-1]:
        if eachnumber % 2 == 0:
            numberlist.append(eachnumber)
            if len(numberlist) == n:
                numberlist.reverse()
                return numberlist

