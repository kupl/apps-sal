def head_smash(arr):
    if isinstance(arr, int):
        return "This isn't the gym!!"
    return [line.replace('O', ' ') for line in arr] if arr else 'Gym is empty'
