def whatday(num):
    dic = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    return dic[num] if num in dic.keys() else 'Wrong, please enter a number between 1 and 7'
