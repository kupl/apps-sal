def men_from_boys(arr):
    """this is not the most elegant or concise solution, but it is functional"""
    even_men = []
    odd_boys = []
    boys_men = []
    for number in arr:
        if number % 2 == 0:
            even_men.append(number)
        else:
            odd_boys.append(number)
    even_men = set(even_men)
    odd_boys = set(odd_boys)
    even_men = list(even_men)
    odd_boys = list(odd_boys)
    even_men.sort()
    odd_boys.sort(reverse=True)
    for number in even_men:
        boys_men.append(number)
    for number in odd_boys:
        boys_men.append(number)
    return boys_men
