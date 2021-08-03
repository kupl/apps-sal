def whatday(num):
    d = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
    try:
        return d[num]
    except KeyError:
        return "Wrong, please enter a number between 1 and 7"
