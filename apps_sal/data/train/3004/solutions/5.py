def head_smash(arr):
    if isinstance(arr, int) is True:
        return "This isn\'t the gym!!"

    elif arr == [] or arr == '':
        return 'Gym is empty'
    
    else:
        d = [x.replace('O', ' ') for x in arr]
        return d
