def whatday(num):
    err = "Wrong, please enter a number between 1 and 7"
    try:
        return [err, "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][int(num)]
    except:
        return err
