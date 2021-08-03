def whatday(num):
    if num <= 0 or num >= 8:
        return "Wrong, please enter a number between 1 and 7"

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days[num - 1]
