def whatday(num):
    lst = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return lst[num - 1] if 0 < num < 8 else "Wrong, please enter a number between 1 and 7"
