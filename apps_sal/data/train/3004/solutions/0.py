def head_smash(arr):
    try:
        return [a.replace('O', ' ') for a in arr] or 'Gym is empty'
    except TypeError:
        return "This isn't the gym!!"
