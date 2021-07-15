def odd_or_even(liste):
    somme = sum(i for i in liste)
    if somme % 2 ==0:
        return 'even'
    else:
        return 'odd'
