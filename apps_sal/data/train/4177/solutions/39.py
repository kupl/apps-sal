def men_from_boys(arr):
    men = [_ for _ in set(arr) if _ % 2 == 0]
    men =  sorted(men)
    boys = [_ for _ in set(arr) if _ % 2 != 0]
    boys = sorted(boys)
    boys.reverse()
    res = []
    
    return men + boys
