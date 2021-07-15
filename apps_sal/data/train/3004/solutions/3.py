import re
def head_smash(arr):
    try:
        return [re.sub('O',' ',i) for i in arr] if arr else 'Gym is empty'
    except:
        return 'This isn\'t the gym!!'
