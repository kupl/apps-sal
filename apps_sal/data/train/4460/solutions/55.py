def whatday(num):
    try:
        a = zip(range(1, 8), ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
        adict = dict(a)
        return adict[num]
    except:
        return "Wrong, please enter a number between 1 and 7"
