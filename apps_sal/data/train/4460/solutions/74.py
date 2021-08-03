def whatday(n):
    if 0 < n < 8:

        return['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'][n - 1].title()
    else:
        return "Wrong, please enter a number between 1 and 7"
