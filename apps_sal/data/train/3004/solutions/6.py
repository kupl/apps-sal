def head_smash(arr):
    if not arr:
        return 'Gym is empty'
    if not isinstance(arr, list) or not all((isinstance(l, str) for l in arr)):
        return "This isn't the gym!!"
    return [l.replace('O', ' ') for l in arr]
