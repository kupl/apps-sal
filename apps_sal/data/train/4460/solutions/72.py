def whatday(num):
    print(num)
    days = {
        1: "Sunday", 
        2: "Monday", 
        3: "Tuesday", 
        4: "Wednesday", 
        5: "Thursday", 
        6: "Friday", 
        7: "Saturday"}
    return days.get(num) if num in days.keys() else "Wrong, please enter a number between 1 and 7"
