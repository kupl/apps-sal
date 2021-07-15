wd = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
def whatday(num):
    return wd[num-1] if num-1 in range(7) else "Wrong, please enter a number between 1 and 7"
