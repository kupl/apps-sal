def head_smash(arr):
    try:
        return [x.replace('O', ' ') for x in arr] or 'Gym is empty'
    except:
        return "This isn't the gym!!"
