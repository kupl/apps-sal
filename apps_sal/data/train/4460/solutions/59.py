def whatday(num):
    if num <= 0 or num > 7:
        return "Wrong, please enter a number between 1 and 7"
    weekdays = ["", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return weekdays[num]
