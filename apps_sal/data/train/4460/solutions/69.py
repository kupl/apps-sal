def whatday(num):
    
    day = ["Wrong, please enter a number between 1 and 7","Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    if num <= 7:
        return day[num]
    
    else:
        return "Wrong, please enter a number between 1 and 7"
