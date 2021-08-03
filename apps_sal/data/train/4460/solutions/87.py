def whatday(num):
    l = [0, 'Sunday', "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return "Wrong, please enter a number between 1 and 7" if num > 7 or num < 1 else l[num]
