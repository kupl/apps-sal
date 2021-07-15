def head_smash(arr):
    if not arr:
        return 'Gym is empty'
    if isinstance(arr, int):
        return "This isn't the gym!!"
    return [l.replace('O', ' ') for l in arr]
