def head_smash(arr):
    if not arr:
        return 'Gym is empty'
    if not isinstance(arr, list):
        return "This isn't the gym!!"
    return list(map(lambda x: x.replace('O', ' '), arr))
