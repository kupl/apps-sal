def whatday(num):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if num > 7 or num <= 0:
        return "Wrong, please enter a number between 1 and 7"
    for index, x in enumerate(days, 1):
        if num == index:
            return x
#         if 0 >= num > 7:
#             return "Wrong, please enter a number between 1 and 7"

